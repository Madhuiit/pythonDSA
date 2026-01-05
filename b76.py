#replaces specific value
import pandas as pd

df = pd.DataFrame({"A":[1,2,2,3]})

df["A"].replace(2,99,inplace=True)
print(df.drop_duplicates())

