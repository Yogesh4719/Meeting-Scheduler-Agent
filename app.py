import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Smart Scheduler", layout="centered")

st.title("📅 Intelligent Meeting Scheduler")
st.write("Optimizes meeting times using calendar compression + preference scoring.")

# ---------------- Helper Functions ----------------

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def format_time(dt):
    return dt.strftime("%H:%M")

def compress_busy_slots(busy_slots):
    busy_slots = sorted(busy_slots, key=lambda x: x[0])
    compressed = []

    for start, end in busy_slots:
        if not compressed:
            compressed.append((start, end))
        else:
            last_start, last_end = compressed[-1]
            if start <= last_end:
                compressed[-1] = (last_start, max(last_end, end))
            else:
                compressed.append((start, end))

    return compressed

def get_free_slots(working_start, working_end, busy_slots):
    free_slots = []
    current = working_start

    for start, end in busy_slots:
        if current < start:
            free_slots.append((current, start))
        current = max(current, end)

    if current < working_end:
        free_slots.append((current, working_end))

    return free_slots

def filter_by_duration(free_slots, duration_minutes):
    valid_slots = []
    for start, end in free_slots:
        total_minutes = (end - start).seconds // 60
        if total_minutes >= duration_minutes:
            valid_slots.append((start, start + timedelta(minutes=duration_minutes)))
    return valid_slots

def score_slot(slot, preference):
    score = 0
    hour = slot[0].hour

    if preference == "Morning" and 9 <= hour < 12:
        score += 3
    elif preference == "Afternoon" and 12 <= hour < 17:
        score += 3
    elif preference == "Evening" and 17 <= hour <= 19:
        score += 3

    return score

# ---------------- UI Inputs ----------------

st.subheader("Working Hours")

col1, col2 = st.columns(2)
with col1:
    work_start = parse_time(st.text_input("Start Time (HH:MM)", "09:00"))
with col2:
    work_end = parse_time(st.text_input("End Time (HH:MM)", "18:00"))

st.subheader("Busy Slots")
busy_input = st.text_area(
    "Enter busy slots (Format: 09:00-10:00, 12:00-13:00)",
    "09:00-10:00, 12:00-13:30, 16:00-17:00"
)

meeting_duration = st.number_input("Meeting Duration (minutes)", min_value=15, value=60)

preference = st.selectbox("Preferred Time", ["Morning", "Afternoon", "Evening"])

# ---------------- Scheduler Logic ----------------

if st.button("Find Best Meeting Time"):

    busy_slots = []
    if busy_input.strip():
        for slot in busy_input.split(","):
            start_str, end_str = slot.strip().split("-")
            busy_slots.append((parse_time(start_str), parse_time(end_str)))

    compressed_busy = compress_busy_slots(busy_slots)
    free_slots = get_free_slots(work_start, work_end, compressed_busy)
    valid_slots = filter_by_duration(free_slots, meeting_duration)

    st.subheader("📊 Compressed Busy Slots")
    for start, end in compressed_busy:
        st.write(f"{format_time(start)} - {format_time(end)}")

    if not valid_slots:
        st.error("No available slots for this duration.")
    else:
        scored = [(slot, score_slot(slot, preference)) for slot in valid_slots]
        scored.sort(key=lambda x: x[1], reverse=True)

        best_slot = scored[0][0]

        st.success("✅ Best Meeting Slot Found!")
        st.write(f"### Suggested: {format_time(best_slot[0])} - {format_time(best_slot[1])}")
        st.write(f"Reason: Matches preferred time '{preference}'")

        st.write("### Alternative Options:")
        for slot, score in scored[1:4]:
            st.write(f"{format_time(slot[0])} - {format_time(slot[1])}")
