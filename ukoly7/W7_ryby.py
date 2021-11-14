import requests
import pandas
import statsmodels.formula.api as smf
import seaborn
import matplotlib.pyplot as plt

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/Fish.csv")
with open("Fish.csv", "wb") as f:
  f.write(r.content)

df = pandas.read_csv("Fish.csv")
print(df.head())
print(df.columns)
print(df.dtypes)
['Species', 'Weight', 'Length1', 'Length2', 'Length3', 'Height','Width']

#Ryby
#V souboru Fish.csv najdeš informace o rybách z rybího trhu: délku (vertikální - Length1, diagonální - Length2 a úhlopříčnou - Length3), výšku, šířku, živočišný druh ryby, hmnotnost ryby.
#a)Vytvoř regresní model, který bude predikovat hmnotnost ryby na základě její diagonální délky (sloupec Length2).
mod = smf.ols(formula="Weight ~ Length2", data=df)
res = mod.fit()
print(res.summary())
#R-squared je 84,4%

#b)Zkus přidat do modelu výšku ryby (sloupec Height) a porovnej, jak se zvýšila kvalita modelu.
mod = smf.ols(formula="Weight ~ Length2 + Height", data=df)
res = mod.fit()
print(res.summary())
#R-squared je 87,5% (tj. přídáním parametru výška se model zpřesnil)

#c)Nakonec pomocí metody target encoding zapracuj do modelu živočišný druh ryby.
print(df["Species"].unique())
print(df.groupby("Species")["Weight"].mean().sort_values())
prumer_vaha_druh = df.groupby("Species")["Weight"].mean()
df["prumer_vaha_druh"] = df["Species"].map(prumer_vaha_druh)
mod = smf.ols(formula="Weight ~ Length2 + Height + prumer_vaha_druh ", data=df)
res = mod.fit()
print(res.summary())
#R-squared je 90% (tj. přídáním parametru průměrné váhy ryba daného druhu se model vylepšil)