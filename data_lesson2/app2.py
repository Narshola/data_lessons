import pandas as pd

df = pd.read_csv("GoogleApps.csv")

#1
print(df.groupby(by = "Type")["Rating"].agg(["min", "median", "max"]))

#2
temp = df[df["Type"] == "Paid"]
print(temp.groupby(by = "Content Rating")["Price"].agg(["min", "median", "max"]))

#3
temp1 = df.groupby(by = "Category")["Reviews"].max()
temp2 = df.groupby(by = "Content Rating")["Reviews"].max()
print(temp1)
print(temp2)