import pandas as pd 

df  = pd.DataFrame({"Sales":[100,200,300]})


df["cumulative"]=df["Sales"].cumsum()

df["Parcentage"]= df["Sales"]/df["Sales"].sum()*100
print(df)kvkvv 