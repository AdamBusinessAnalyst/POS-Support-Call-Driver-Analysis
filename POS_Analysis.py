import sys

import pandas as pd

DATA_FILE = "mock_pos_data.csv"


def main() -> None:
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print(f"Error: '{DATA_FILE}' not found.")
        sys.exit(1)
    print(f"Loaded {len(df)} tickets.\n")

    print("--- Top Call Drivers (share of tickets by subcategory) ---")
    volume = df["issue_subcategory"].value_counts()
    print((volume / len(df) * 100).round(1).astype(str) + "%")

    print("\n--- Avg Resolution Time (minutes) by Category ---")
    efficiency = (
        df.groupby("issue_category")["resolution_time_min"].mean().round(1)
    )
    print(efficiency)

    print("\n--- Share of Total Agent Time by Category ---")
    time_share = (
        df.groupby("issue_category")["resolution_time_min"].sum()
        / df["resolution_time_min"].sum()
        * 100
    )
    print(time_share.round(1).astype(str) + "%")

    print("\n--- High Impact Issues (avg minutes per subcategory) ---")
    impact = (
        df.groupby("issue_subcategory")["resolution_time_min"]
        .mean()
        .sort_values(ascending=False)
    )
    print(impact.round(1))

    print("\n--- Automated Recommendations ---")
    top_volume = volume.idxmax()
    slowest = efficiency.idxmax()
    fastest = efficiency.idxmin()
    ratio = efficiency[slowest] / efficiency[fastest]
    print(
        f"1. High volume: '{top_volume}' is the most common issue. "
        "Consider self-service tools or automation."
    )
    print(
        f"2. High effort: '{slowest}' tickets take {ratio:.1f}x longer than "
        f"'{fastest}' ones. Consider targeted troubleshooting guides."
    )


if __name__ == "__main__":
    main()
