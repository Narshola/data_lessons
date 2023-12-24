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
        return "Actor-Director"
    i += 1
    return "Without Actor-Director"

df["Actors"] = df["Actors"].apply(lambda x: x.split(','))
df["Actor-Director"] = df["Director"].apply(director_to_actor)

actor_director = df[df["Actor-Director"] == "Actor-Director"]["Metascore"].mean()
without_actor_director = df[df["Actor-Director"] == "Wirgout Actor-Director"]["Metascore"].mean()

print(actor_director)
print(without_actor_director)

print(actor_director - without_actor_director)

df["Actor-Director"].value_counts().plot(kind="pie")
plt.show()

temp = df.groupby(by="Actor-Director")["Metascore"].mean()
temp.plot(kind="bar")
plt.show()

temp = df.pivot_table(columns="Actor-Director",
                      values="Metascore",
                      aggfunc="mean")
print(temp)

temp.plot(kind="barh", figsize=(8, 5))
plt.show()

#У фильмов с большим метражом рейтинг выше, чем у фильмов с меньшим метражом. (Да, на 0.6)
def runtime_status(value):
    if value < df["Runtime (Minutes)"].mean():
        return "Less Runtime"
    return "More Runtime"

df["Runtime Status"] = df["Runtime (Minutes)"].apply(runtime_status)
temp = df.pivot_table(columns="Runtime Status",
                      values="Rating",
                      aggfunc="mean")
temp.plot(kind="barh")
plt.show()

#У старых фильмов голосов больше, чем у новых.
def check_year(value):
    if value < df["Year"].mean():
        return "Old"
    return "New"

df["Year Status"] = df["Year"].apply(check_year)
temp = df.pivot_table(columns="Year Status",
                      values="Votes",
                      aggfunc="mean")
print(temp)

temp.plot(kind="barh")
plt.show()

#У старых фильмов выше доход, чем у новых (Да)
df["Revenue (Millions)"].fillna(df["Revenue (Millions)"].mean(), inplace=True)

temp = df.pivot_table(columns="Year Status",
                      values="Revenue (Millions)",
                      aggfunc="mean")

temp.plot(kind="barh")
plt.show()