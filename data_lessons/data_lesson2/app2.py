import pandas as pd

df = pd.read_csv("GoogleApps.csv")

#1
print(df.groupby(by = "Type")["Rating"].agg(["min", "mean", "max"]))

#2
temp = df[df["Type"] == "Paid"]
print(temp.groupby(by = "Content Rating")["Price"].agg(["min", "median", "max"]))

#3
temp_categories = df[(df["Category"] == "EDUCATION") | (df["Category"] == "FAMILY") | (df["Category"] == "GAME")]
temp = temp_categories.pivot_table(columns="Category",
                      index="Content Rating",
                      values="Reviews",
                      aggfunc='max')
print(temp)

#4
temp_paid = df[df["Type"] == "Paid"]
temp = temp_paid.pivot_table(columns="Content Rating",
                             index="Category",
                             values="Reviews",
                             aggfunc='mean')
print(temp)

# #5
temp_free = df[df["Type"] == "Free"]
temp = temp_free.pivot_table(columns="Content Rating",
                              index="Category",
                              values="Reviews",
                              aggfunc='mean')
print(temp)