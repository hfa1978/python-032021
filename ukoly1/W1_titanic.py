"""
Titanic
V souboru tested.csv najdeš informace o cestujících na zaoceánském parníku Titanic. Vytvoř kontingenční tabulku, která porovná závislost mezi pohlavím cestujícího (soupec Sex), třídou (sloupec Pclass), ve které cestoval, a tím, jesti přežil potopení Titanicu (sloupec Survived). Pro data můžeš použít agregaci numpy.sum, která ti spočte absolutní počet přeživších pro danou kombinaci, nebo numpy.mean, která udá relativní počet přeživších pro danou kombinaci.
"""

import pandas
import requests
import numpy

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/titanic.csv")
open("titanic.csv", 'wb').write(r.content)

cestujici = pandas.read_csv("titanic.csv")
#print(cestujici.columns)
#print(cestujici.head())
# Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#       dtype='object')

cestujici_pivot1 = pandas.pivot_table(cestujici, values="Survived", index="Pclass", columns="Sex", aggfunc=numpy.sum, margins=True)
print(cestujici_pivot1)

cestujici_pivot2 = pandas.pivot_table(cestujici, values="Survived", index="Pclass", columns="Sex", aggfunc=numpy.mean, margins=True)
print(cestujici_pivot2)
