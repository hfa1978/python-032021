import pandas
import requests
import seaborn
import matplotlib.pyplot as plt

#V souboru crypto_prices.csv najdeš ceny různých kryptoměn v průběhu času. Datum je ve sloupci Date a název kryptoměny ti prozradí sloupec Name, alternativně můžeš využít sloupec Symbol.

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)
kryptomeny = pandas.read_csv("crypto_prices.csv")
#print(kryptomeny.head())
#print(kryptomeny.columns)
# SNo', 'Name', 'Symbol', 'Date', 'High', 'Low', 'Open', 'Close','Volume', 'Marketcap', 'FileName

#1.Použij zavírací cenu kryptoměny (sloupec Close) a vypočti procentuální změnu jednotlivých kryptoměn. Pozor na to, ať se ti nepočítají ceny mezi jednotlivými měnami. Ošetřit to můžeš pomocí metody groupby(), jako jsme to dělali např. u metody shift().
kryptomeny.groupby(["Symbol"])["Date"].rank(ascending=False)
kryptomeny["Close_vcera"] = kryptomeny.groupby(["Symbol"])["Close"].shift()
#print(kryptomeny[["Symbol","Date","Close", "Close_vcera"]])
#print(kryptomeny.loc[kryptomeny["SNo"] ==1])
kryptomeny["Zmena"] = (kryptomeny["Close"]-kryptomeny["Close_vcera"])/kryptomeny["Close_vcera"]
print(kryptomeny[["Symbol","Date","Close", "Close_vcera", "Zmena"]])

#2.Vytvoř korelační matici změn cen jednotlivých kryptoměn a zobraz je jako tabulku.
kpivot = kryptomeny.pivot_table(index="Date", columns="Symbol", values="Zmena", aggfunc="min")
print(kpivot.corr())

#3.V tabulce vyber dvojici kryptoměn s vysokou hodnotou koeficientu korelace a jinou dvojici s koeficientem korelace blízko 0. Změny cen pro dvojice měn, které jsou nejvíce a nejméně korelované, si zobraz jako bodový graf.

#nízká korelace DOGE / CRO
vyber1 = kpivot[["DOGE", "CRO"]]
vyber1_change = vyber1.pct_change()
#print(vyber1_change)
seaborn.jointplot(x="DOGE", y="CRO", data=vyber1_change, kind='scatter')
plt.show()

#vysoká korelace BTC a WBTC
vyber2 = kpivot[["BTC", "WBTC"]]
vyber2_change = vyber2.pct_change()
seaborn.jointplot(x="BTC",y="WBTC", data=vyber2_change, kind='scatter')
plt.show()

