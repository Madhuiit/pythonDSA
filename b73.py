import pandas as pd
df = pd.DataFrame({"A":[10,40,30,20]})

print(df.nlargest(2,"A"))

print(df.nsmallest(2,"A"))

