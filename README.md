# Bluestock Mutual Fund Analytics Capstone

## Project Overview

This project builds an end-to-end Mutual Fund Analytics Platform using Python, SQLite, and Power BI. The objective is to analyze mutual fund performance, investor behavior, SIP trends, and risk-adjusted returns through a complete data engineering and analytics workflow.

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* Matplotlib
* Power BI
* Git & GitHub

## Project Architecture

Raw Data → Data Cleaning → ETL Pipeline → SQLite Database → Analytics & Metrics → Power BI Dashboard

## Datasets Used

1. Fund Master
2. NAV History
3. Benchmark Indices
4. Industry Folio Counts
5. Monthly SIP Inflows
6. Scheme Performance
7. Fund Scorecard
8. Investor Transactions

## Folder Structure

```text
data/
├── raw/
├── processed/

scripts/
notebooks/
sql/
dashboard/
reports/
```

## How to Run

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

## Dashboard Pages

### Page 1 – Industry Overview

* Total AUM KPI
* SIP Inflows KPI
* Folio Count KPI
* Industry AUM Trend
* AMC Comparison

### Page 2 – Fund Performance

* Risk vs Return Scatter Plot
* Fund Scorecard Ranking
* NAV vs Benchmark
* Fund Slicers

### Page 3 – Investor Analytics

* State-wise Investment Analysis
* Transaction Distribution
* Age Group Analysis
* Monthly Investment Trend

### Page 4 – SIP & Market Trends

* SIP Inflow Trend
* NIFTY50 Comparison
* Category Inflow Analysis

## Key Findings

* Mutual fund industry showed consistent AUM growth.
* Equity-oriented funds generated higher returns.
* Sharpe Ratio helped identify superior risk-adjusted performers.
* SIP participation increased steadily.
* Interactive dashboards improved decision-making visibility.

## Deliverables

* ETL Pipeline
* SQLite Database
* EDA Analysis
* Performance Analytics
* Advanced Analytics
* Power BI Dashboard
* Final Report
* Presentation

## Author

Anil Velma

Bluestock Mutual Fund Analytics Capstone Project
