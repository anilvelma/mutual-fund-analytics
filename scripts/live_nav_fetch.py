import requests
import pandas as pd 

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print(data.keys())
print(data["meta"])
nav_df = pd.DataFrame(data["data"])
print(nav_df.head())
print(nav_df.shape)

nav_df.to_csv(
    "../data/raw/hdfc_top100_live_nav.csv",
    index=False
)
print("CSV Saved Successfully")