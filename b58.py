import pandas as pd

df = pd.DataFrame({"Category":["A","A","B","B"],"Sales":[100,200,300,400]})

pivot = df.pivot_table(values="Sales",index="Category",aggfunc="sum")

print(pivot)





