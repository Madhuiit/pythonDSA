import pandas as pd

df = pd.DataFrame({
    "Date":["2023-01-01","2023-02-01"]
})

df["Date"] = pd.to_datetime(df["Date"])

print(df.dtypes)

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

print(df)