#apply custom function to column

import pandas as pd


df = pd.DataFrame({"A":[1,2,3]})

df["Squar"] = df["A"].apply(lambda x:x**2)

print(df)