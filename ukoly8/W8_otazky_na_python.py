import pandas
import requests
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.seasonal import seasonal_decompose

#a)Stáhni si soubor MLTollsStackOverflow.csv, který obsahuje počty položených otázek na jednotlivé programovací techniky a další technologie.
r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/MLTollsStackOverflow.csv")
with open("MLTollsStackOverflow.csv", "wb") as f:
  f.write(r.content)
df = pandas.read_csv("MLTollsStackOverflow.csv")

#b)Vyber sloupec python.
df = df[["month","python"]]
print(df)

#c)Proveď dekompozici této časové řady pomocí multiplikativního modelu. Dekompozici zobraz jako graf.
decompose = seasonal_decompose(df['python'], model='multiplicative', period=12)
decompose.plot()
plt.show()

#d)Vytvoř predikci hodnot časové řady pomocí Holt-Wintersovy metody na 12 měsíců. Sezónnost nastav jako 12 a uvažuj multiplikativní model pro trend i sezónnost. Výsledek zobraz jako graf.
mod = ExponentialSmoothing(df["python"], seasonal_periods=12, trend="add", seasonal="add", use_boxcox=True, initialization_method="estimated",)
res = mod.fit()
df_forecast = pandas.DataFrame(res.forecast(12), columns=["Prediction"])
df_with_prediction = pandas.concat([df, df_forecast])
df_with_prediction[["python", "Prediction"]].plot()
plt.show()