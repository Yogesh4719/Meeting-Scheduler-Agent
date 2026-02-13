# Meeting-Scheduler-Agent
# 📅 Intelligent Scheduling System

An intelligent meeting scheduling web application that compresses calendar data and optimizes meeting time selection using preference-based heuristic scoring.

Built using Python and Streamlit.

---

## 🚀 Project Overview

This system takes:

- Working hours  
- Busy time slots  
- Meeting duration  
- User time preference (Morning / Afternoon / Evening)  

It then:

1. Compresses overlapping busy intervals  
2. Calculates available free time slots  
3. Filters slots based on meeting duration  
4. Applies preference-based scoring  
5. Suggests the most optimal meeting time  

The system is designed to reduce computational overhead by compressing calendar intervals before performing optimization, improving scheduling efficiency and reducing latency.

---

## 🧠 Key Features

- ✅ Calendar interval compression  
- ✅ Free slot calculation  
- ✅ Constraint-based filtering  
- ✅ Preference-driven optimization  
- ✅ Alternative meeting suggestions  
- ✅ Interactive web UI  

---

## 🏗️ Tech Stack

- **Python**
- **Streamlit**
- **datetime module**
- Interval merging algorithms
- Heuristic optimization logic

---

## ⚙️ How It Works

1. **Interval Compression**
   - Merges overlapping busy time slots to reduce redundant computations.

2. **Free Slot Calculation**
   - Subtracts busy intervals from working hours.

3. **Constraint Filtering**
   - Removes slots shorter than required meeting duration.

4. **Preference Scoring**
   - Assigns higher scores to slots matching user preference.

5. **Best Slot Selection**
   - Selects highest-scoring slot and provides alternatives.

---

## 🖥️ Run Locally

### 1️⃣ Clone the Repository

```bash
git clone YOUR_REPO_LINK
cd smart_scheduler
