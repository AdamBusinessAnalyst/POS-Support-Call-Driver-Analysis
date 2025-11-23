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

# 4. Identify "High Impact" Issues
# Issues that are frequent AND take a long time (High Volume + High Effort)
print("\n--- High Impact Issues (Avg Time per Subcategory) ---")
impact_analysis = df.groupby('issue_subcategory')['resolution_time_min'].mean().sort_values(ascending=False)
print(impact_analysis)

# 5. Recommendation Logic based on findings
print("\n--- Automated Recommendations ---")
high_volume_issue = volume_analysis.idxmax()
slowest_issue = efficiency_analysis.idxmax()

print(f"1. High Volume: '{high_volume_issue}' is the most common issue. Consider self-service tools or automation.")
print(f"2. High Effort: '{slowest_issue}' issues take the longest to resolve. Consider targeted agent training.")