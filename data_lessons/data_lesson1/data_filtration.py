import pandas as pd

df = pd.read_csv('GoogleApps.csv')

#1
print(df[df['Type']=='Paid']["Price"].min())

#2
print(df[df['Category']=='ART_AND_DESIGN']["Installs"].median())

#3
print(df[df["Type"]=="Free"]["Reviews"].max() - df[df["Type"]=="Paid"]["Reviews"].max())

#4
print(df[df["Content Rating"]=="Teen"]["Size"].min())

#5
print(df[df["Reviews"] == df["Reviews"].max()]["Category"])

#6 
print(df[(df["Price"]>20.0) & (df["Installs"]>10000.0)]["Rating"].mean())