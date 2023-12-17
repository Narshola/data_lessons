import pandas as pd
import matplotlib.pyplot as plt

#Генератор занимательных идей о киноиндустрии

#Какие неожиданные факты о киноиндустрии можно получить?

df = pd.read_csv("IMDB-Movie-Data.csv")
print(df.info())


#Присутствие определённой комбинации "актёр-режиссёр" повышает рейтинг фильма на метакритик. (Да, на 0.45)

i = 0
def director_to_actor(value):
    global i
    if value in df["Actors"].iloc[i]:
        i += 1
        return 1
    i += 1
    return 0

df["Actors"] = df["Actors"].apply(lambda x: x.split(','))
df["Actor-Director"] = df["Director"].apply(director_to_actor)

print(df[df["Actor-Director"] == 0]["Metascore"].mean())
print(df[df["Actor-Director"] == 1]["Metascore"].mean())

print(df[df["Actor-Director"] == 1]["Metascore"].mean() - 
      df[df["Actor-Director"] == 0]["Metascore"].mean())

df["Actor-Director"].value_counts().plot(kind="pie")
plt.show()

temp = df.groupby(by="Actor-Director")["Metascore"].mean()
temp.plot(kind="bar")
plt.show()

#У фильма с самым большим метражом рейтинг выше среднего значения. (Да, на 0.8768)
print(df[df["Runtime (Minutes)"] == df["Runtime (Minutes)"].max()]["Rating"])
print(df[df["Runtime (Minutes)"] == df["Runtime (Minutes)"].max()]["Rating"]-df["Rating"].mean())

#У фильмов с большим метражом рейтинг выше, чем у фильмов с меньшим метражом. (Да, на 0.6)
print(df[df["Runtime (Minutes)"] > df["Runtime (Minutes)"].mean()]["Rating"].mean() - 
      df[df["Runtime (Minutes)"] < df["Runtime (Minutes)"].mean()]["Rating"].mean())

#У старых фильмов голосов больше, чем у новых. (Нет, среднее значение у старых меньше на ~147724)

#У новых фильмов голосов больше, чем у старых.
def check_year(value):
    pass

df["Year Status"] = df["Year"].apply()

#У старых фильмов выше доход, чем у новых (Да)
df["Revenue (Millions)"].fillna(df["Revenue (Millions)"].mean(), inplace=True)

print(df[df["Year"] < df["Year"].mean()]["Revenue (Millions)"].mean())
print(df[df["Year"] > df["Year"].mean()]["Revenue (Millions)"].mean())