import pandas as pd
df = pd.DataFrame({"Fruit":["Apple","Banana","Apple"]})

print(pd.get_dummies(df,columns=["Fruit"]))