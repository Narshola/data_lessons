import pandas as pd

#Очистка из data_cleaning.py
df = pd.read_csv("GooglePlayStore_wild.csv")

def no_str(value):
    if value == 'Varies with device':
        value = '-1.0'
        return float(value)
    if 'M' in value:
        return float(value[:-1])
    if 'k' in value:
        return float(value[:-1]) / 1024
    return 0

def make_installs(value):
    value = value[:-1]
    if ',' in value:
        value = value.replace(',', '')
        return value
    if value == '':
        return 0

df["Rating"].fillna(-1, inplace = True)
df["Size"] = df["Size"].apply(no_str)
df["Installs"] = df['Installs'].apply(make_installs)
df["Installs"].fillna(0, inplace=True)
df['Installs'] = df["Installs"].apply(int)
df["Type"].fillna("Free", inplace=True)

#1
def make_price(value):
    value = value[1:]
    if value == '':
        value = 0.0
        return value
    return float(value)
df["Price"] = df["Price"].apply(make_price)
df["Profit"] = df["Installs"] * df["Price"]
print(df[df["Type"] == "Paid"]["Profit"].max())

#2
def genres_to_list(value):
    return value.split(';')
df["Genres"] = df["Genres"].apply(genres_to_list)
df["Number Of Genres"] = df["Genres"].apply(len)
print(df["Number Of Genres"].max())

#3
def last_upd_to_list(value):
    return value.split(' ')

def season(value):
    value = value[0]
    if value in ["December", "January", "February"]:
        return "Winter"
    if value in ["March", "April", "May"]:
        return "Spring"
    if value in ["June", "July", "August"]:
        return "Summer"
    else:
        return "Autumn"

df["Last Updated"] = df["Last Updated"].apply(last_upd_to_list)
df["Season"] = df["Last Updated"].apply(season)
print(df["Season"].value_counts())