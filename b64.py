import pandas as pd

df = pd.DataFrame({
    "A": [1,None,3],"B":[4,5,None]
})

print(df.dropna())

# fill missing values with mean 

df["A"].fillna(df["A"].mean(),inplace=True)
df["B"].fillna(df["B"].mean() , inplace=True)

print(df)