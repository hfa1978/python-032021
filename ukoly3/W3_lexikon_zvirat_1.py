#Lexikon zvířat 1
#Načti si soubor pomocí metody read_csv. Pozor, tento dataset využívá jako oddělovač středník, nikoliv čárku. Při načítání dat proto nastav parametr sep na znak středníku (";"). Poslední sloupec a poslední řádek obsahují nulové hodnoty. Zbav se tohoto sloupce a řádku. Nastav sloupec id jako index pomocí metody set_index.

import pandas
import requests
r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)
zvirata = pandas.read_csv("lexikon-zvirat.csv", sep=";")
zvirata = zvirata.dropna(how="all", axis="columns")
zvirata = zvirata.dropna(how="all", axis="rows")
print(zvirata)
zvirata = zvirata.set_index("id")
print(zvirata)

#Dataset obsahuje sloupec image_src, který má jako hodnoty odkazy na fotky jednotlivých zvířat. Například odkaz https://zoopraha.cz/images/lexikon-images/Drozd_oranIovohlav_.jpg vede na fotku drozda oranžovohlavého. Napiš funkci check_url, která bude mít jeden parametr radek. Funkce zkontroluje, jestli je odkaz v pořádku podle několika pravidel. K odkazu přistoupíš v těle funkce přes tečkovou notaci: radek.image_src. Zkontroluj následující:
#datový typ je řetězec: isinstance(radek.image_src, str)
#hodnota začíná řetězcem "https://zoopraha.cz/images/": radek.image_src.startswith("https://zoopraha.cz/images/")
#hodnota končí buďto JPG nebo jpg.
#Zvol si jeden ze způsobů procházení tabulky, a na každý řádek zavolej funkci check_url. Pro každý řádek s neplatným odkazem vypiš název zvířete (title).
#print(zvirata[["title", "image_src"]])
def check_url(radek):
  if isinstance(radek.image_src, str):
    if radek.image_src.startswith("https://zoopraha.cz/images/"):
      if radek.image_src.endswith("jpg") or radek.image_src.endswith("JPG"):
        return radek
for radek in zvirata.itertuples():
  if not check_url(radek):
    print(radek.title)