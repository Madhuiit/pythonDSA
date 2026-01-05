import pandas as pd

df1 = pd.DataFrame({"A":[1,2]})

df2 = pd.DataFrame({"A":[3,4]})

print(pd.concat([df1,df2]))