#merge two Dataframe on key
import pandas as pd
df1 = pd.DataFrame({"Id":[1,2],"Name":["A","B"]})

df2 = pd.DataFrame({"Id":[1,2],"Age":[25,30]})
print(pd.merge(df1,df2,on="Id"))





