import pandas as pd
import os

data_path = "../data/raw"

files = sorted([f for f in os.listdir(data_path) if f.endswith(".csv")]) #This finds all CSV files automatically.

for file in files:
    print("\n" + "=" * 80)
    print(f"DATASET: {file}")
    print("=" * 80)

    try:
        df = pd.read_csv(os.path.join(data_path, file))

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}: {e}")