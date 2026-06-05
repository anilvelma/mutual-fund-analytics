# Mutual Fund Analytics - Day 2 Report

## Project Overview

The objective of this phase was to clean the raw mutual fund datasets, validate data quality, design a database schema, and load the cleaned data into a SQLite database for further analysis and dashboard development.

---

## Data Cleaning Activities

### 1. NAV History Dataset

* Converted date column to datetime format.
* Sorted records by AMFI code and date.
* Forward-filled missing NAV values.
* Removed duplicate records.
* Validated that all NAV values are greater than zero.

### 2. Investor Transactions Dataset

* Standardized transaction types (SIP, Lumpsum, Redemption).
* Validated transaction amounts are greater than zero.
* Fixed transaction date formats.
* Verified KYC status values.
* Removed duplicate records.

### 3. Scheme Performance Dataset

* Validated return columns as numeric values.
* Checked expense ratio range (0.1% to 2.5%).
* Flagged return anomalies.
* Removed duplicate records.

### 4. Remaining Datasets

* Removed duplicate records.
* Standardized text columns.
* Saved cleaned versions in the processed data folder.

---

## Processed Datasets

1. fund_master_cleaned.csv
2. nav_history_cleaned.csv
3. investor_transactions_cleaned.csv
4. scheme_performance_cleaned.csv
5. aum_by_fund_house_cleaned.csv
6. monthly_sip_inflows_cleaned.csv
7. category_inflows_cleaned.csv
8. industry_folio_count_cleaned.csv
9. portfolio_holdings_cleaned.csv
10. benchmark_indices_cleaned.csv

---

## SQLite Database Design

Database Name:
bluestock_mf.db

### Dimension Tables

* dim_fund
* dim_date

### Fact Tables

* fact_nav
* fact_transactions
* fact_performance
* fact_aum

Primary keys and foreign keys were defined to support analytical queries using a star schema design.

---

## Database Loading Summary

| Table                 | Rows Loaded |
| --------------------- | ----------- |
| fund_master           | 40          |
| nav_history           | 45,962      |
| investor_transactions | 32,778      |
| scheme_performance    | 40          |
| aum_by_fund_house     | 90          |
| monthly_sip_inflows   | 48          |
| category_inflows      | 144         |
| industry_folio_count  | 21          |
| portfolio_holdings    | 322         |
| benchmark_indices     | 8,050       |

---

## Data Quality Summary

* All AMFI codes validated successfully.
* No invalid transaction types found.
* No invalid KYC status values found.
* No negative transaction amounts found.
* No invalid expense ratios found.
* No missing return values found.
* Data successfully loaded into SQLite database.

---

## Deliverables Completed

* 10 cleaned CSV files
* SQLite database (bluestock_mf.db)
* schema.sql
* queries.sql
* data_dictionary.md
* GitHub repository updated

## Conclusion

Day 2 focused on data cleaning, validation, database schema design, and database loading. All required datasets were processed successfully and loaded into SQLite for future analytics, dashboard development, and reporting.
