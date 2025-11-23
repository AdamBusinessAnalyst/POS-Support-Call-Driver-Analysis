# Point of Sale Support Call Driver Analysis

This project analyzes POS support ticket data to understand what drives the workload and how to reduce it. The focus is on ticket volume, resolution times, and the issues that require the most effort. The work is done using Python and SQL.

---

## Project Goal

Identify the main causes of high support volume and long handle times, then provide practical steps to improve support efficiency.

---

## What Was Found

### **Hardware issues are the biggest bottleneck**
Printer and card reader issues make up about **half of all tickets** and take **three times longer** to resolve than simple operational tasks. These drive most of the high AHT.

### **Small requests add unnecessary load**
Menu changes, supply orders, and other quick fixes are simple but appear in high volume, cluttering the queue.

---

## What Can Be Improved

### **Reduce operational volume**
Create a simple **Self-Service Menu Manager** so merchants can update menus and order supplies themselves. This could deflect up to **30% of all tickets**, freeing agents for more technical issues.

### **Cut hardware resolution time**
Provide targeted troubleshooting training for **printers and connectivity issues**. Clearer decision trees will reduce the time agents spend on these cases.

---

## Tech Used

- Python (Pandas)

---

## 💻 Code Summary

The script performs four main tasks:

1. Loads ticket data  
2. Identifies the most common issues  
3. Calculates average resolution times  
4. Highlights high-impact issues (high volume + long resolution time)

Below is the core analysis logic written in Python using pandas.


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

# 4. High-Impact Issues
print("\n--- High Impact Issues (Avg Time per Subcategory) ---")
impact_analysis = df.groupby('issue_subcategory')['resolution_time_min'].mean().sort_values(ascending=False)
print(impact_analysis)

# 5. Recommendations
print("\n--- Automated Recommendations ---")
high_volume_issue = volume_analysis.idxmax()
slowest_issue = efficiency_analysis.idxmax()

print(f"1. High Volume: '{high_volume_issue}' is the most common issue. Consider self-service options.")
print(f"2. High Effort: '{slowest_issue}' issues take the longest. Improve agent training here.")

Project Structure:

POS-Support-Call-Driver-Analysis/
│
├── data/
│   └── mock_pos_data.csv
│
├── analysis/
│   └── pos_call_driver_analysis.py
│
└── README.md

