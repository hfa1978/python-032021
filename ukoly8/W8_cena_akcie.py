import pandas
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.graphics.tsaplots import plot_acf

#Cena akcie
#Pomocí modulu yfinance, který jsme používali v 5. lekci, stáhni ceny akcií společnosti Cisco (používají "Ticker" CSCO) za posledních 5 let. Dále pracuj s cenami akcie v závěru obchodního dne, tj. použij sloupec "Close".
csco = yf.Ticker("CSCO")
df = csco.history(period="5y")
df = df.reset_index()
df["Date"] = pandas.to_datetime(arg=df["Date"],format="%Y-%m-%d")
df = df.set_index(["Date"])
print(df)
#print(df.dtypes)

#a)Zobraz si graf autokorelace a podívej se, jak je hodnota ceny závislná na svých vlastních hodnotách v minulosti.
df["Close"].autocorr(lag=7)
plot_acf(df["Close"])
plt.show()

#b)Zkus použít AR model k predikci cen akcie na příštích 5 dní.
model = AutoReg(df['Close'], lags=7, trend="ct", seasonal=True, period=12)
model_fit = model.fit()
predictions = model_fit.predict(start=df.shape[0], end=df.shape[0] + 5)
df_forecast = pandas.DataFrame(predictions, columns=["Prediction"])
df_with_prediction = pandas.concat([df, df_forecast])
print(df_with_prediction.tail())

#c)Zobraz v grafu historické hodnoty (nikoli celou řadu, ale pro přehlednost např. hodnoty za posledních 50 dní) a tebou vypočítanou predikci.
df_with_prediction[["Close", "Prediction"]].tail(50).plot()
plt.show()
