import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "data" / "raw" / "02_nav_history.csv"

df = pd.read_csv(input_file)

print("Original Shape:", df.shape)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")

# Sort by AMFI code and date
df = df.sort_values(["amfi_code", "date"])

# Convert NAV to numeric
df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

# Forward fill missing NAV values within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicate rows
df = df.drop_duplicates()

# Keep only valid NAV values (> 0)
df = df[df["nav"] > 0]

print("Cleaned Shape:", df.shape)

# Check remaining missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Save cleaned dataset
output_file = BASE_DIR / "data" / "processed" / "nav_history_cleaned.csv"

df.to_csv(output_file, index=False)

print("\nCleaned file saved successfully!")