"""
Titanic
V souboru tested.csv najdeš informace o cestujících na zaoceánském parníku Titanic. Vytvoř kontingenční tabulku, která porovná závislost mezi pohlavím cestujícího (soupec Sex), třídou (sloupec Pclass), ve které cestoval, a tím, jesti přežil potopení Titanicu (sloupec Survived). Pro data můžeš použít agregaci numpy.sum, která ti spočte absolutní počet přeživších pro danou kombinaci, nebo numpy.mean, která udá relativní počet přeživších pro danou kombinaci.
 Z dat vyfiltruj pouze cestující, kteří cestovali v první třídě. Dále použij metodu cut na rozdělení cestujících do věkových skupin (zkus vytvořit např. 4 skupiny, můžeš definovat hranice skupin tak, aby vznikly skupiny děti, teenageři, dospělí a senioři). Urči relativní počet přeživších pro jednotlivé kombinace pohlavní a věkové skupiny.
"""

import pandas
import requests
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)
cestujici = pandas.read_csv("titanic.csv")

cestujici_1trida = cestujici.loc[cestujici["Pclass"]==1]
print(cestujici_1trida)
#rint(cestujici.max())
#print(cestujici.min())

cestujici["Age_group"] = pandas.cut(cestujici["Age"], bins=[0,12,19,65,100])
cestujici_pivot3 = pandas.pivot_table(cestujici, values="Survived", index="Age_group", columns="Sex", aggfunc=numpy.mean, margins=True)
print(cestujici_pivot3)
