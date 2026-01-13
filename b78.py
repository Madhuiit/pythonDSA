import pandas as pd 

df  = pd.DataFrame({"Sales":[100,200,300]})


df["cumulative"]=df["Sales"].cumsum()

df["percentage"] = df["Sales"]/df["Sales"].sum()*100


Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)


IQR = Q3 - Q1

outliars = df[(df["Sales"] < Q1 - 1.5*IQR)| (df["Sales"]> Q3+1.5*IQR)]

print(outliars)

print(df)

df["Zscore"] = (df["Sales"] - df["Sales"].mean())/df["Sales"].std()

print(df)