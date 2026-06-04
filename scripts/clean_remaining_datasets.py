import pandas as pd

files = {
    "01_fund_master.csv": "fund_master_cleaned.csv",
    "03_aum_by_fund_house.csv": "aum_by_fund_house_cleaned.csv",
    "04_monthly_sip_inflows.csv": "monthly_sip_inflows_cleaned.csv",
    "05_category_inflows.csv": "category_inflows_cleaned.csv",
    "06_industry_folio_count.csv": "industry_folio_count_cleaned.csv",
    "09_portfolio_holdings.csv": "portfolio_holdings_cleaned.csv",
    "10_benchmark_indices.csv": "benchmark_indices_cleaned.csv"
}

for input_file, output_file in files.items():

    df = pd.read_csv(f"../data/raw/{input_file}")

    print(f"\nProcessing: {input_file}")
    print("Original Shape:", df.shape)

    # Remove duplicates
    df = df.drop_duplicates()

    # Trim text columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()

    print("Cleaned Shape:", df.shape)

    df.to_csv(
        f"../data/processed/{output_file}",
        index=False
    )

    print(f"Saved: {output_file}")

print("\nAll datasets cleaned successfully!")