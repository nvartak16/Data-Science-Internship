import pandas as pd
df = pd.read_csv("IRIS.csv")
print(df)
df.info()
print(df.head(20))
print(df.tail(10))
print(df.columns.values)
print(df.describe())
print(df.loc[:,["petal_length","species"]])
print(df[df["petal_width"]>0.1])
print(df[50:100])