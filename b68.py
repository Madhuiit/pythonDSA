import pandas as pd

df = pd.DataFrame({
    "A":[1,2,2,3],"B":[4,5,5,6]
})

print(df.drop_duplicates())