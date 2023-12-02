import pandas as pd


df = pd.read_csv("GoogleApps.csv")

#1
print(df["Category"].value_counts())

#2
temp = df["Content Rating"].value_counts()
print(temp["Teen"] / temp["Everyone 10+"])

#3
temp = df.groupby(by = "Type")["Rating"].mean()
print(temp)
print(temp["Paid"] - temp["Free"])

#4
temp = df.groupby(by = "Category")["Size"].agg(["min", "max"])
print(temp)

#5
temp = df[df["Rating"] > 4.5]["Category"].value_counts()
print(temp["FINANCE"])

temp1 = df[(df["Rating"] > 4.9) & (df["Type"] == "Free")]["Category"].value_counts()
temp2 = df[(df["Rating"] > 4.9) & (df["Type"] == "Paid")]["Category"].value_counts()
print(temp1["GAME"] / temp2["GAME"])