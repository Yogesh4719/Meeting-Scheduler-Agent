📅 Intelligent Scheduling System

An intelligent meeting scheduling web application that compresses calendar data and optimizes meeting time selection using preference-based heuristic scoring.

Built using Python and Streamlit.

🚀 Project Overview

This system accepts:

Working hours

Busy time slots

Meeting duration

Preferred time of day (Morning / Afternoon / Evening)

It then:

Compresses overlapping busy intervals

Calculates available free slots

Filters slots based on meeting duration

Applies preference-based scoring

Suggests the optimal meeting time with alternatives

The system reduces computational overhead by merging calendar intervals before performing scheduling optimization, improving efficiency and reducing latency.

🧠 Key Features

✅ Calendar interval compression

✅ Free slot calculation

✅ Constraint-based filtering

✅ Preference-driven optimization

✅ Alternative meeting suggestions

✅ Interactive web interface

🏗️ Tech Stack

Python

Streamlit

datetime module

Interval merging algorithms

Heuristic scoring logic

⚙️ How It Works
1️⃣ Interval Compression

Overlapping busy time slots are merged to reduce redundant calculations.

2️⃣ Free Slot Calculation

Busy intervals are subtracted from working hours to generate available slots.

3️⃣ Constraint Filtering

Slots shorter than the required meeting duration are removed.

4️⃣ Preference Scoring

Time slots matching user preference are given higher scores.

5️⃣ Best Slot Selection

The highest-scoring slot is selected and alternative options are displayed.
