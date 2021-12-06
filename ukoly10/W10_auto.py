"""Pracuj se souborem auto.csv. Obsahuje informace o vyráběných modelech aut mezi lety 1970-1982."""

import pandas
import requests
import matplotlib.pyplot as plt
from sklearn.metrics import (accuracy_score, confusion_matrix, ConfusionMatrixDisplay, f1_score, precision_score, recall_score,
)
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import LinearSVC

#1. Načti data. Při volání metody read_csv nastav parametr na_values: na_values=["?"]. Neznámé/prázdné hodnoty jsou totiž reprezentované jako znak otazníku. Po načtení dat se zbav řádek, které mají nějakou neznámou/prázdnou hodnotu (nápověda: dropna).
r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/auto.csv")
open("auto.csv", "wb").write(r.content)
data = pandas.read_csv("auto.csv", na_values=["?"])
#print(data.columns)
#print(data.dtypes)
#print(data.shape)
#print(data.isna().sum())
#print(data.shape)
data = data.dropna()
#print(data.shape)

#2. Naše výstupní proměnná bude sloupec "origin". Pod kódy 1, 2 a 3 se skrývají regiony USA, Evropa a Japonsko. Zkus odhadnout (třeba pomocí sloupce "name"), který region má který kód :-)
#print(data[["origin", "name"]].loc[data["origin"]==1])
#1 - odhaduji na USA
#print(data[["origin", "name"]].loc[data["origin"]==2])
#2 - odhaduji na Evropu
#print(data[["origin", "name"]].loc[data["origin"]==3])
#3 - odhaduji na Japonsko

#3. Podívej se, jak se měnila spotřeba aut v letech 1970-1982. Vytvoř graf, který ukáže průměrnou spotřebu v jednotlivých letech (graf může být sloupcový nebo čarový, a může ukazovat celkovou průměrnou spotřebu, nebo, jako dobrovolný doplněk, zobraz spotřebu tak, aby byly rozlišené tři regiony).
data.groupby("year")["mpg"].mean().plot(kind="bar")
plt.show()

#4. Rozděl data na vstupní a výstupní proměnnou, a následně na trénovací a testovací sadu v poměru 70:30.
X = data.drop(columns=["year"])
y = data["year"]
encoder = OneHotEncoder()
X = encoder.fit_transform(X)
print(X.shape)
print(y.shape)
X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.3, random_state=42)
print (X_train)

#5. Data normalizuj:
scaler = StandardScaler(with_mean=False)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print (X_train)

#6. Použij klasifikační algoritmus rozhodovacího stromu, a vyber jeho parametry technikou GridSearchCV:
#clf = DecisionTreeClassifier(max_depth=2, min_samples_leaf=1, random_state=0)
model = DecisionTreeClassifier(random_state=0)
clf = GridSearchCV(model, param_grid={"max_depth":[1,2,3,4], "min_samples_leaf":[1,2]})
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f1_score(y_test, y_pred, average="weighted"))

#7. Jaké jsi dosáhl/a metriky f1_score?
#78%