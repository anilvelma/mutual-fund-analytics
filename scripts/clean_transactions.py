import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# ----------------------------------
# Fix Date Format
# ----------------------------------
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# ----------------------------------
# Standardize Transaction Types
# ----------------------------------
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

valid_transaction_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

print("\nTransaction Types:")
print(df["transaction_type"].unique())

# Flag invalid transaction types
invalid_txns = df[
    ~df["transaction_type"].isin(valid_transaction_types)
]

print("\nInvalid Transaction Types:", len(invalid_txns))

# ----------------------------------
# Validate Amount > 0
# ----------------------------------
invalid_amounts = df[df["amount_inr"] <= 0]

print("Invalid Amount Records:", len(invalid_amounts))

# Keep only positive amounts
df = df[df["amount_inr"] > 0]

# ----------------------------------
# Check KYC Status Values
# ----------------------------------
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

invalid_kyc = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print("\nInvalid KYC Records:", len(invalid_kyc))

# ----------------------------------
# Remove Duplicates
# ----------------------------------
df = df.drop_duplicates()

print("\nCleaned Shape:", df.shape)

# ----------------------------------
# Save Clean Dataset
# ----------------------------------
df.to_csv(
    "../data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("\nFile Saved Successfully!")