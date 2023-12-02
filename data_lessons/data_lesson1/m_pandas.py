import pandas as pd

df = pd.read_csv('GoogleApps.csv')

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(round(df["Installs"].mean(), 2))
print(df["Installs"].median())
print(df["Price"].max())

print(df[df['Type']=='Paid']["Price"].min())
print(df[df['Category']=='ART_AND_DESIGN']["Installs"].median())
print(df[df["Type"]=="Free"]["Reviews"].max() - df[df["Type"]=="Paid"]["Reviews"].max())
print(df[df["Content Rating"]=="Teen"]["Size"].min())
print(df[(df["Price"]>20.0) & (df["Installs"]>10000.0)]["Rating"].mean())