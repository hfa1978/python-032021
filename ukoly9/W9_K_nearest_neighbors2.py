"""Stáhni si dataset kosatce.csv, který obsahuje pozorování o dvou typech kosatce. Jako vstupní proměnné pro předpověď typu kosatce ( Setosa a Virginica) máme délku kalichu a délku okvětního lístku. Výstupní proměnná je označená jako target.

Načti si data do proměnných X a y
Rozděl data na trénovací a testovací (velikost testovacích dat nastav na 30% a nezapomeň nastavit proměnnou random_state, aby tvoje výsledky byly reprodukovatelné)
Pokud použijeme stejný algoritmus jako v prvním úkolu, tj. KNeighborsClassifier, je možné předpovědět typ kosatce na základě těchto dat tak, aby metrika f1_score dosáhla alespoň 85%?"""

import pandas
import requests
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score, precision_score, recall_score, ConfusionMatrixDisplay,)

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/kosatce.csv")
open("kosatce.csv", "wb").write(r.content)
data = pandas.read_csv("kosatce.csv")

X = data.drop(columns=["target"])
y = data["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
print(clf)
y_pred = clf.predict(X_test)
print(y_pred)
print(confusion_matrix(y_true=y_test, y_pred=y_pred))
ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test, display_labels=clf.classes_, cmap=plt.cm.Blues,)
plt.show()
print(f1_score(y_test, y_pred))

ks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(k, f1_score(y_test, y_pred))

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f1_score(y_test, y_pred))

""" Ano, pro hodnotu parametru k= 1,3,5,7,9,11 je to 86%)"""