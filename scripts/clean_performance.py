import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# -----------------------------
# Return Columns
# -----------------------------
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

# Convert returns to numeric
for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check for non-numeric values
print("\nMissing values after numeric conversion:")
print(df[return_cols].isnull().sum())

# -----------------------------
# Expense Ratio Validation
# -----------------------------
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nFunds with invalid expense ratio:")
print(len(invalid_expense))

# -----------------------------
# Anomaly Detection
# -----------------------------
anomalies = df[
    (df["return_1yr_pct"] > 100) |
    (df["return_1yr_pct"] < -100)
]

print("\nPotential Return Anomalies:")
print(len(anomalies))

if len(anomalies) > 0:
    print(anomalies[[
        "amfi_code",
        "scheme_name",
        "return_1yr_pct"
    ]])

# -----------------------------
# Remove Duplicates
# -----------------------------
df = df.drop_duplicates()

print("\nCleaned Shape:", df.shape)

# -----------------------------
# Save Clean Dataset
# -----------------------------
df.to_csv(
    "../data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("\nFile Saved Successfully!")