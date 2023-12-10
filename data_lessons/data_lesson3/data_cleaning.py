import pandas as pd

df = pd.read_csv('GooglePlayStore_wild.csv')

#1
print(df.info())

#2
print(pd.isnull(df["Rating"]).value_counts())
df["Rating"].fillna(-1, inplace = True)
print(pd.isnull(df["Rating"]).value_counts())

#3
def no_str(value):
    if value == 'Varies with device':
        value = '-1.0'
        return float(value)
    if 'M' in value:
        return float(value[:-1])
    if 'k' in value:
        return float(value[:-1]) / 1024
    return 0

print(df["Size"].value_counts())
df["Size"] = df["Size"].apply(no_str)
print(df["Size"].value_counts())
print(df[df["Category"] == "TOOLS"]["Size"].max())

#4
def make_installs(value):
    value = value[:-1]
    if ',' in value:
        value = value.replace(',', '')
        return value
    if value == '':
        return -1
df["Installs"] = df['Installs'].apply(make_installs)
df["Installs"].fillna(-1, inplace=True)
df['Installs'] = df["Installs"].apply(int)
print(df["Installs"].value_counts())

temp = df.pivot_table(columns="Type",
                      index="Content Rating",
                      values="Installs",
                      aggfunc="mean")
print(temp)

#5
print(df[pd.isnull(df["Type"]) == True]["App"])
print(df[pd.isnull(df["Type"]) == True]["Price"])
df["Type"].fillna("Free", inplace=True)
print(df[df["App"] == "Command & Conquer: Rivals"]["Type"])

#6
df2 = pd.read_csv('googleplaystore.csv')
temp = df2.iloc[10472]
i = 12
while i > 0:
    temp.iloc[i] = temp.iloc[i-1]
    i -= 1
df2.iloc[10472] = temp
print(df2.iloc[10472])