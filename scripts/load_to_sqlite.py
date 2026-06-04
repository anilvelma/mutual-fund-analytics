import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///../bluestock_mf.db")

files = {
    "fund_master_cleaned.csv": "fund_master",
    "nav_history_cleaned.csv": "nav_history",
    "investor_transactions_cleaned.csv": "investor_transactions",
    "scheme_performance_cleaned.csv": "scheme_performance",
    "aum_by_fund_house_cleaned.csv": "aum_by_fund_house",
    "monthly_sip_inflows_cleaned.csv": "monthly_sip_inflows",
    "category_inflows_cleaned.csv": "category_inflows",
    "industry_folio_count_cleaned.csv": "industry_folio_count",
    "portfolio_holdings_cleaned.csv": "portfolio_holdings",
    "benchmark_indices_cleaned.csv": "benchmark_indices"
}

for file_name, table_name in files.items():

    df = pd.read_csv(f"../data/processed/{file_name}")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name}: {len(df)} rows loaded")

print("\nAll datasets loaded successfully!")