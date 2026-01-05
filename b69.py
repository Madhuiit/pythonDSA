import pandas as pd
df = pd.DataFrame({"Category":["A","A","B"],"Sales":[100,200,300]})

print(df.groupby("Category")["Sales"].sum())
