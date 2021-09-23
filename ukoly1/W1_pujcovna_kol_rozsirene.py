"""
Půjčování kol
V souboru london_merged.csv najdeš informace o počtu vypůjčení jízdních kol v Londýně.

Vytvoř sloupec, do kterého z časové značky (sloupec timestamp) ulož rok.
Vytvoř kontingenční tabulku, která porovná kód počasí (sloupec weather_code se sloupcem udávající rok.
Definice jednotlivých kódů jsou:

1 = Clear ; mostly clear but have some values with haze/fog/patches of fog/ fog in vicinity
2 = scattered clouds / few clouds
3 = Broken clouds
4 = Cloudy
7 = Rain/ light Rain shower/ Light rain
10 = rain with thunderstorm
26 = snowfall
94 = Freezing Fog

Jako hodnoty v kontingenční tabulce zobraz relativní počty jízd pro jednotlivé kódy počasí v jednom roce. Příklad možného výsledku by byl: v roce 2020 proběhlo 40 % jízd za počasí s kódem 1, 20 % jízd za počasí s kódem 2 a 40 % jízd za počasí s kódem 3 atd. Postup, jak na to, najdeš v v lekci v části označené jako "Čtení na doma".
"""
import pandas
import requests
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
open("london_merged.csv", 'wb').write(r.content)

pujcovna = pandas.read_csv("london_merged.csv")
pujcovna["timestamp"] = pandas.to_datetime(pujcovna["timestamp"])
pujcovna["year"] = pujcovna["timestamp"].dt.year

pujcovna_pivot = pandas.pivot_table(pujcovna, index="weather_code", columns="year", values="cnt",aggfunc=numpy.sum, margins=True)

pujcovna_pivot_procenta = pujcovna_pivot.div(pujcovna_pivot.iloc[:,-1], axis=0)
print(pujcovna_pivot_procenta)