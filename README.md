POS Support Call Driver Analysis

This project breaks down POS support ticket data to understand what’s driving the workload and how to reduce it. The analysis focuses on ticket volume, resolution times, and the issues that take the most effort. Everything is done using Python and SQL.

🎯 Project Goal

Identify the real causes behind high support volume and long handle times, then suggest practical steps to improve support efficiency.

📊 What I Found
1. Hardware issues are the biggest bottleneck

Printer and card reader problems account for about half of all tickets and take three times longer to resolve compared to simple operational tasks. This is the biggest contributor to high AHT.

2. Small requests add unnecessary load

Menu changes, supply orders, and other quick fixes are low-complexity, but they show up in high volume and clutter the queue.

🚀 What to Improve
1. Reduce operational volume

Build a simple Self-Service Menu Manager where merchants can update menus and order supplies. This could deflect up to 30% of all tickets, letting agents focus on real technical issues.

2. Cut hardware resolution time

Give Tier 1 agents stronger troubleshooting training specifically for printers and connectivity problems. Clearer decision trees can bring down time spent on these cases.

🛠 Tech Used

Python (Pandas)

## Analysis Code

The core analysis is performed using Python and the pandas library.

```python
import pandas as pd

# 1. Load the Data
try:
    df = pd.read_csv('mock_pos_data.csv')
    print("Data loaded successfully.\n")
except FileNotFoundError:
    print("Error: 'mock_pos_data.csv' not found.")
    exit()

# 2. Analyze Top Call Drivers (Volume)
print("--- Top Call Drivers (By Subcategory) ---")
# counting specific issues like 'Printer', 'Menu', 'Connectivity'
volume_analysis = df['issue_subcategory'].value_counts()
print(volume_analysis)

# 3. Analyze Efficiency (Average Resolution Time)
print("\n--- Avg Resolution Time (Minutes) by Category ---")
# Determining if Hardware issues take longer than Operational ones
efficiency_analysis = df.groupby('issue_category')['resolution_time_min'].mean().round(1)
print(efficiency_analysis)

# ... (rest of the script)
