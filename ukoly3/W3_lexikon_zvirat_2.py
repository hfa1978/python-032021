#Lexikon zvířat 2
#Načti si soubor pomocí metody read_csv. Pozor, tento dataset využívá jako oddělovač středník, nikoliv čárku. Při načítání dat proto nastav parametr sep na znak středníku (";"). Poslední sloupec a poslední řádek obsahují nulové hodnoty. Zbav se tohoto sloupce a řádku. Nastav sloupec id jako index pomocí metody set_index.

import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)
zvirata = pandas.read_csv("lexikon-zvirat.csv", sep=";")
zvirata = zvirata.dropna(how="all", axis="columns")
zvirata = zvirata.dropna(how="all", axis="rows")
#print(zvirata)
zvirata = zvirata.set_index("id")
#print(zvirata)

#Chceme ke každému zvířeti vytvořit popisek na tabulku do zoo. Popisek bude využívat sloupců title (název zvířete), food (typ stravy), food_note (vysvětlující doplněk ke stravě) a description (jak zvíře poznáme). Napiš funkci popisek, která bude mít jeden parametr radek. Funkce spojí informace dohromady. Následně použijte metodu apply, abyste vytvořili nový sloupec s tímto popiskem.
#print(zvirata[["title", "food", "food_note", "description"]])

def popisek(radek):
  cast1 = f"{radek.title} preferuje následující typ stravy: "
  cast2 = f"{radek.food}. "
  cast3 = f"Konkrétně ocení, když mu do misky přistanou {radek.food_note}. \n"
  cast4 = f"Jak toto zvíře poznáme: {radek.description}"
  popisek_text = cast1 + cast2 + cast3 + cast4
  return(popisek_text)
#for radek in zvirata.itertuples():
  #print(popisek(radek))

zvirata["cedulka"] = zvirata.apply(popisek,axis=1)
print(zvirata[["cedulka"]].iloc[320])
print(zvirata[["cedulka"]].iloc[300])
#zvirata.to_excel("zvirata.xlsx")