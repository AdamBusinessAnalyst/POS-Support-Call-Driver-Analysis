# Point of Sale Support Call Driver Analysis

> **Data Notice:** All data in `mock_pos_data.csv` is entirely synthetic and was programmatically generated for demonstration purposes. It does not represent real customers, transactions, or business records.

This project analyzes POS support ticket data to understand what drives the workload and how to reduce it. The focus is on ticket volume, resolution times, and the issues that require the most effort.

---

## Project Goal

Identify the main causes of high support volume and long handle times, then provide practical steps to improve support efficiency.

---

## What Was Found

### Hardware issues are the biggest bottleneck
Printer and card reader issues make up about **half of all tickets** and take **three times longer** to resolve than simple operational tasks.

### Small requests add unnecessary load
Menu changes, supply orders, and other quick fixes are simple but appear in high volume, cluttering the queue.

---

## What Can Be Improved

### Reduce operational volume
Create a **Self-Service Menu Manager** so merchants can update menus and order supplies themselves. This could deflect up to **30% of all tickets**, freeing agents for more technical issues.

### Cut hardware resolution time
Provide targeted troubleshooting guides for printers and connectivity issues. Clearer decision trees reduce the time agents spend on these cases.

---

## Tech Used

- Python (Pandas)

---

## Code Summary

The script performs four main tasks:

1. Loads ticket data
2. Identifies the most common issues
3. Calculates average resolution times
4. Highlights high-impact issues (high volume + long resolution time)

\`\`\`python
import pandas as pd

df = pd.read_csv('mock_pos_data.csv')

# Volume analysis
volume_analysis = df['issue_subcategory'].value_counts()

# Resolution time by category
efficiency_analysis = df.groupby('issue_category')['resolution_time_min'].mean().round(1)

# High-impact issues
impact_analysis = df.groupby('issue_subcategory')['resolution_time_min'].mean().sort_values(ascending=False)

# Automated recommendations
high_volume_issue = volume_analysis.idxmax()
slowest_issue = efficiency_analysis.idxmax()
print(f"High Volume: '{high_volume_issue}' — consider self-service options.")
print(f"High Effort: '{slowest_issue}' — improve agent training here.")
\`\`\`

---

## Project Structure

\`\`\`
POS-Support-Call-Driver-Analysis/
├── .github/workflows/
│   └── python-app.yml
├── POS_Analysis.py
├── mock_pos_data.csv
└── README.md
\`\`\`
