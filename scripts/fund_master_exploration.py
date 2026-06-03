import pandas as pd

df = pd.read_csv("../data/raw/01_fund_master.csv")

print("Shape:")
print(df.shape)

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nNumber of Fund Houses:")
print(df["fund_house"].nunique())

print("\nCategories:")
print(df["category"].unique())

print("\nNumber of Categories:")
print(df["category"].nunique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nNumber of Sub Categories:")
print(df["sub_category"].nunique())

print("\nRisk Categories:")
print(df["risk_category"].unique())

print("\nNumber of Risk Categories:")
print(df["risk_category"].nunique())

print("\nSample AMFI Codes:")
print(df["amfi_code"].head(10))

print("\nUnique AMFI Codes:")
print(df["amfi_code"].nunique())