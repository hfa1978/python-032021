"""
K Nearest Neighbors 1
Zopakuj experiment, ale tentokrát vyber hodnotu parametru n_neighbors na základě metriky precision. Znamená to, že pro nás bude důležité, abychom raději označili pitnou vodu za nepitnou, než nepitnou za pitnou. Raději nebudeme pít vůbec, než abychom se napili nepitné vody a onemocněli.
V podstatě bude potřeba upravit krok 6. Upravení parametrů modelu. Na základě číselných hodnot nebo grafu vyber tu hodnotu parametru, která dává nejlepší výsledek (nejvyšší hodnotu při volání precision()).
Liší se tvůj zvolený parametr od parametru, který jsme jako závěrečný zvolili v lekci?
Jak vypadá matice chyb (confusion matrix)? Dovedeš z matice odvodit výpočet, který nám dá stejnou hodnotu, jako při použití metody precision()?
"""

import pandas
import requests
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score, precision_score, recall_score, ConfusionMatrixDisplay,)

#krok 1 - definice problému
r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/water-potability.csv")
open("water-potability.csv", 'wb').write(r.content)
#Je vodat pitná či není pitná_

#krok 2 - příprava dat
data = pandas.read_csv("water-potability.csv")
data = data.dropna()
X = data.drop(columns=["Potability"])
y = data["Potability"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print (X_train)
#krok 3,4 - výběr algoritmu a trénování modelu
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
print(clf)
#krok 5 - vyhodnocení modelu
y_pred = clf.predict(X_test)
print(y_pred)
print(confusion_matrix(y_true=y_test, y_pred=y_pred))
ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test, display_labels=clf.classes_, cmap=plt.cm.Blues,)
plt.show()
print(precision_score(y_test, y_pred))
#krok 6 - upravení parametru modelu
ks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
precision_scores = []
f1_scores = []
for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    precision_scores.append(precision_score(y_test, y_pred))
    #print(k, precision_score(y_test, y_pred))
for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    f1_scores.append(f1_score(y_test, y_pred))
    #print(k, f1_score(y_test, y_pred))
plt.plot(ks, f1_scores, precision_scores)
plt.show()

# krok 7 - závěrečná predikce
clf = KNeighborsClassifier(n_neighbors=15)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(precision_score(y_test, y_pred))

"""Při výběru metriky precision score je parametr k=15 (u f1_score metriky to bylo k=3). Confusion matrix se nezměnila.
Matice je TP=97, TN=283, FP=72, FN=152
Otázce: Dovedeš z matice odvodit výpočet, který nám dá stejnou hodnotu, jako při použití metody precision? úplně nerozumím, 
zda je to 97/(97+72)?"""