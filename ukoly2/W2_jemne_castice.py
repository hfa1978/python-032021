""" Jemné částice
V souboru air_polution_ukol.csv najdeš data o množství jemných částic změřených v ovzduší v jedné plzeňské meteorologické stanici."""

import pandas
import requests
import numpy
import matplotlib.pyplot as plt
import seaborn

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)
air_polution = pandas.read_csv("air_polution_ukol.csv")
print(air_polution.head())
#print(air_polution.dtypes)

"""1.Načti dataset a převeď sloupec date (datum měření) na typ datetime."""
air_polution["date"] = pandas.to_datetime(air_polution["date"], format="%Y/%m/%d")
print(air_polution.head())
#print(air_polution.dtypes)

"""2.Přidej sloupce s rokem a číslem měsíce, které získáš z data měření."""
air_polution["year"] = air_polution["date"].dt.year
air_polution["month"] = air_polution["date"].dt.month
print(air_polution.head())
#print(air_polution.dtypes)

"""3. Vytvoř pivot tabulku s průměrným počtem množství jemných částic (sloupec pm25) v jednotlivých měsících a jednotlivých letech. Jako funkci pro agregaci můžeš použít numpy.mean."""
air_polution_pivot_1 = pandas.pivot_table(air_polution, index="year", columns="month", values="pm25", aggfunc=numpy.sum, margins=False)
print(air_polution_pivot_1)

"""Doplněk 1: Podívej se do první lekce na část o teplotních mapách a zobrat výsledek analýzy jako teplotní mapu."""
seaborn.heatmap(air_polution_pivot_1, annot=False, fmt=".5f", linewidths=.5, cmap="YlGn")
plt.show()

"""Doplněk 2: Použij metodu dt.dayofweek a přidej si do sloupce den v týdnu. Číslování je od 0, tj. pondělí má číslo 0 a neděle 6. Porovnej, jestli se průměrné množství jemných částic liší ve všední dny a o víkendu."""
air_polution["dayofweek"] = air_polution["date"].dt.dayofweek
air_polution_pivot_2 = pandas.pivot_table(air_polution, index="month", columns="dayofweek", values="pm25", aggfunc=numpy.sum, margins=True)
print(air_polution_pivot_2)