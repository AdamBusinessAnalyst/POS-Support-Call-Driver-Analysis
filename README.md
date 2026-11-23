# POS Support Call Driver Analysis

What drives support workload for a restaurant POS product, and where is agent time going?

> **Data notice:** `mock_pos_data.csv` is synthetic (100 tickets). It does not represent real customers or business records.

## Key findings

| Metric | Hardware | Network | Operational |
|---|---|---|---|
| Share of tickets | 38% | 19% | 43% |
| Avg resolution time | 63.8 min | 52.1 min | 13.5 min |
| Share of total agent time | **60.7%** | 24.8% | 14.5% |

- **Hardware is the bottleneck.** 38% of tickets but 61% of agent time. Hardware tickets take **4.7x longer** than operational ones.
- **Printer and device failures** together are 29% of all tickets. Installations are rare (9%) but the slowest at ~98 min each.
- **Menu changes and supply orders** are 32% of tickets but take 6–11 min each: high volume, low effort, easy to self-serve.

## Recommendations

1. **Self-service menu manager + supply ordering** — targets the 32% of tickets that are routine merchant requests.
2. **Hardware troubleshooting decision trees** for printers and card readers — targets the category that consumes 61% of agent time.
3. **Pre-install checklist** for merchants — installations are the single slowest ticket type.

## Run it

```bash
pip install -r requirements.txt
python POS_Analysis.py
```

The script prints ticket share by subcategory, average resolution time and share of agent time by category, the highest-effort subcategories, and two auto-generated recommendations.

## Tech

Python, pandas. CI runs flake8 and executes the script on every push.

## Structure

```
POS-Support-Call-Driver-Analysis/
├── .github/workflows/python-app.yml
├── POS_Analysis.py
├── mock_pos_data.csv
├── requirements.txt
└── README.md
```
