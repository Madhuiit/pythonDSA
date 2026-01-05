import pandas as pd

df1 = pd.DataFrame({"id":[1,2],"Name":["A","B"]})

df2 = pd.DataFrame({"id":[1,2],"age":[25,30]})

merged = pd.merge(df1,df2,on="id")

print(merged)


