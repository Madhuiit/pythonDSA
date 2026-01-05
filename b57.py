import pandas as pd

df = pd.DataFrame({"A":[1,2,3,4],"B":[10,20,30,40]})


print(df[(df["A"]>2) & (df["B"]<40)])

