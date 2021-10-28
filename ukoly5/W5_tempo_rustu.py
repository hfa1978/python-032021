import pandas
import requests
import statistics

#Pokračuj v práci s daty o kryptoměnách. Z datového souboru si vyber jednu kryptoměnu a urči průměrné denní tempo růstu měny za sledované období. Můžeš využít funkci geometric_mean z modulu statistics. Vyber si sloupec se změnou ceny, kterou máš vypočítanou z předchozího cvičení (případně si jej dopočti), přičti k němu 1 (nemusíš dělit stem jako v lekci, hodnoty jsou jako desetinná čísla, nikoli jako procenta) a převeď jej na seznam pomocí metody .tolist().
#Následně vypočti geometrický průměr z těchto hodnot.
#Např. pro měnu XMR (Monero) vychází průměrný mezidenní růst ceny na 0.001794558895..

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/crypto_prices.csv")
open("crypto_prices.csv", "wb").write(r.content)
kryptomeny = pandas.read_csv("crypto_prices.csv")
kryptomeny.groupby(["Symbol"])["Date"].rank(ascending=False)
kryptomeny["Close_vcera"] = kryptomeny.groupby(["Symbol"])["Close"].shift()
kryptomeny["Zmena"] = ((kryptomeny["Close"]-kryptomeny["Close_vcera"])/kryptomeny["Close_vcera"])+1
XMR = kryptomeny.loc[kryptomeny["Symbol"]=="XMR"]
XMR = XMR["Zmena"].tolist()
XMR_new = [item for item in XMR if not(pandas.isnull(item))]
print(XMR_new)
prumer = statistics.geometric_mean(XMR_new)
print(prumer)