import pandas as pd

df = pd.read_csv('GoogleApps.csv')

#1
print(df.head())

#2
print(df.tail())

#3
print(df.info())

#4
print(df.describe())

#5
print(round(df["Installs"].mean(), 2))
print(df["Installs"].median())
print(df["Price"].max())