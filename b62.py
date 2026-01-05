import pandas as pd

df = pd.DataFrame({"A":[1,2,3],"B":
[6,5,4],"C":[7,8,9]})
print(df[["A","C"]])


print(df.sort_values("B",ascending=True))

df = df.rename(columns = {
    "A":"Col1","B":"Col2"
})


print(df)



