import pandas as pd

df = pd.DataFrame({"Category":["A","A","B","B"],"Sales":[100,200,300,400]})

df.to_csv("output.csv",index=False)

