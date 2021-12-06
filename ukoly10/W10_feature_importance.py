"""Feature Importance
Pracuj se stejnými daty jako na cvičení, tj. se souborem soybean-2-rot.csv. Níže máš nápovědu. Použij buďto kód níže, nebo tvoje řešení / tvoje parametry.
Rozhodovací strom nám umožňuje nahlédnout do pravidel, podle kterých postupuje ve klasifikaci. Díky tomu se často pokládá za velice průhledný nebo dobře interpretovatelný algoritmus.
Připomeň si, co dělá OneHotEncoder. Kolik proměnných jsme měli původně, a kolik jich máme po "zakódovaní" (nápověda: X.shape)?
Podívej se na atribut feature_importances_ (clf.feature_importances_), který říká, které vstupní proměnné model použil pro rozhodování. Některé budou mít nulovou hodnotu, to znamená, že vůbec potřeba nejsou. Atribut nám dá jen seznam čísel seřazený podle vstupních proměnných, ale ne jejich jména. Ty získáš například z OneHotEncoder: oh_encoder.get_feature_names(input_features=input_features) kde input_features jsou názvy vstupních proměnných před transformací OneHotEncoderem.
Která vstupní proměnná má největší "důležitost"?
Stačí nám tato proměnná pro úspěšnou klasifikaci? Jaký je rozdíl mezi hodnotou f1_score při použití všech proměnných a jen této jedné "nejdůležitější" proměnné?"""

import pandas
import requests
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import (accuracy_score, confusion_matrix, ConfusionMatrixDisplay, f1_score, precision_score, recall_score,
)
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/soybean-2-rot.csv")
open("soybean-2-rot.csv", "wb").write(r.content)
data = pandas.read_csv("soybean-2-rot.csv")
print(data.shape)

X = data.drop(columns=["class"])
input_features = X.columns
#print(input_features)
y = data["class"]
encoder = OneHotEncoder()
X = encoder.fit_transform(X)
data_new = pandas.DataFrame(X.toarray(), columns=encoder.get_feature_names_out())
print(data_new.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
clf = DecisionTreeClassifier(max_depth=5, min_samples_leaf=1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f1_score(y_test, y_pred, average="weighted"))
print(clf.feature_importances_)
print(encoder.get_feature_names(input_features=input_features))

#Odpovědi
#Původní data mají 152 řádků a 24 sloupců.
#One-hot encoder převádí textové proměnné do číselných.
#Nová "převedená" data mají 152 řádků, ale 56 sloupců / 55 proměnných.
#Důležitosti vstupních proměnných - nejdůležitějí je 44% plant-stand.
#Při použití všech proměnných je hodnota f1 score 96,85% (parameter max_depth=5, min_samples_leaf=1)
#Odhaduji - při použití jedné proměnné bude hodnota f1 menší (parametr plant-stand má pouze 2 hodnoty (normal / normal-lt), výstupní proměnná poté 3 (charcoal-rot, phytophthora-rot, brown-stem-rot). Níže výpočet f1-score, bohulže mi to hází u clf.fit(X_train, y_train chybu) - nevím, co je tam špatně

"""
r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/soybean-2-rot.csv")
open("soybean-2-rot.csv", "wb").write(r.content)
data = pandas.read_csv("soybean-2-rot.csv")
data["plant-stand"] = data["plant-stand"].replace({"normal": 1, "lt-normal": 0})
X = data["plant-stand"]
y = data["class"]
print(X.shape)
print(y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
clf = DecisionTreeClassifier(max_depth=5, min_samples_leaf=1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f1_score(y_test, y_pred, average="weighted"))
print(clf.feature_importances_)
print(encoder.get_feature_names(input_features=input_features))
"""