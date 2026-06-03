# Mutual Fund Analytics - Day 1 Data Quality Summary

## Dataset Overview

Total datasets loaded: 10

Datasets:
1. 01_fund_master.csv
2. 02_nav_history.csv
3. 03_aum_by_fund_house.csv
4. 04_monthly_sip_inflows.csv
5. 05_category_inflows.csv
6. 06_industry_folio_count.csv
7. 07_scheme_performance.csv
8. 08_investor_transactions.csv
9. 09_portfolio_holdings.csv
10. 10_benchmark_indices.csv

---

## Fund Master Validation

- Total schemes: 40
- Unique AMFI codes: 40
- Duplicate AMFI codes: 0

---

## Fund House Analysis

Total fund houses: 10

Categories:
- Equity
- Debt

Sub Categories:
- Large Cap
- Small Cap
- Mid Cap
- Flexi Cap
- Value
- ELSS
- Index
- Index/ETF
- Liquid
- Gilt
- Short Duration
- Large & Mid Cap

Risk Categories:
- Low
- Moderate
- Moderately High
- High
- Very High

---

## AMFI Validation

Result:
All AMFI codes from fund_master are present in nav_history.

Validation Status: PASSED

---

## API Data Collection

Successfully fetched:
- Live NAV data using mfapi.in API
- NAV history for 5 key schemes

Schemes:
- SBI Bluechip
- ICICI Bluechip
- Nippon Large Cap
- Axis Bluechip
- Kotak Bluechip

---

## Overall Status

Data ingestion completed successfully.
Datasets are ready for preprocessing and analytics.