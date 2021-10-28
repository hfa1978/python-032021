import pandas
import numpy
from sqlalchemy import create_engine, inspect
import matplotlib.pyplot as plt

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "info"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "KCTiqURc=juzddI0"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)

#Tabulka dreviny v naší databázi obsahuje informace o těžbě dřeva podle druhů dřevin a typu těžby. Objem těžby se nachází ve sloupci hodnota.
dreviny = pandas.read_sql(f"dreviny", con=engine)
#print(dreviny.head())
#1a.Pomocí SQL dotazu do databáze si připrav tabulku smrk, která bude obsahovat řádky, které mají v sloupci dd_txt hodnotu "Smrk, jedle, douglaska
smrk = pandas.read_sql("SELECT * FROM \"dreviny\" WHERE dd_txt = 'Smrk, jedle, douglaska'", con=engine)
#print(smrk)

#1b.Pomocí SQL dotazu do databáze si připrav tabulka nahodila_tezba bude obsahovat řádky, které mají v sloupci druhtez_txt hodnotu "Nahodilá těžba dřeva"
nahodila_tezba = pandas.read_sql("SELECT * FROM \"dreviny\" WHERE druhtez_txt = 'Nahodilá těžba dřeva'", con=engine)
#print(nahodila_tezba[["prictez_txt"]])

#2.Vytvoř graf, který ukáže vývoj objemu těžby pro tabulku smrk. Pozor, řádky nemusí být seřazené podle roku.
smrk.sort_values(by="rok").plot.bar(x="rok", y="hodnota")
plt.show()

#3: Vytvoř graf (nebo několik grafů), který ukáže vývoj objemu těžby v čase pro všechny typy nahodilé těžby. Můžeš použít vlastní postup, nebo postupuj podle jedné z nápověd:
#První metoda: agreguj tabulku nahodila_tezba pomocí metody pivot_table a na výsledek zavolej metodu plot().
#Druhá metoda: agreguj tabulku nahodila_tezba pomocí metody groupby a na výsledek zavolej metodu plot(), kde specifikuješ, který sloupec bude na ose x, a který na ose y.

#nahodila_tezba.groupby(["prictez_txt"]).plot.bar(x="rok", y="hodnota",legend=True)
pandas.pivot_table(nahodila_tezba, index="rok", columns="prictez_txt", values="hodnota", aggfunc=numpy.sum).plot.bar()
plt.show()