import pandas as pd

df = pd.DataFrame({"A":[1,None,3],"B":[None,5,6]})

print(df.isnull().sum())