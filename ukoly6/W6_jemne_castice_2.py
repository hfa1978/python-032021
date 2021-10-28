"""V souboru air_polution_ukol.csv najdeš data o množství jemných částic změřených v ovzduší v jedné plzeňské meteorologické stanici a který jsme již používali v úkolu z druhého týdne.
Pokud máš úkol hotový, můžeš si z něj zkopírovat následující krok: Načti dataset a převeď sloupec date (datum měření) na typ datetime.
Dále pokračuj následujícími kroky:
Z dat vyber data za leden roku 2019 a 2020.
Porovnej průměrné množství jemných částic ve vzduchu v těchto dvou měsících pomocí Mann–Whitney U testu. Formuluj hypotézy pro oboustranný test (nulovou i alternativní) a napiš je do komentářů v programu.
Měl(a) bys dospět k výsledku, že p-hodnota testu je 99 %. Rozhodni, zda bys na hladině významnosti 5 % zamítla nulovou hypotézu. Své rozhodnutí napiš do programu."""

import pandas
import requests
from scipy.stats import mannwhitneyu

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/air_polution_ukol.csv") as r:
  open("air_polution_ukol.csv", 'w', encoding="utf-8").write(r.text)
air_polution = pandas.read_csv("air_polution_ukol.csv")
air_polution["date"] = pandas.to_datetime(air_polution["date"], format="%Y/%m/%d")
air_polution["year"] = air_polution["date"].dt.year
air_polution["month"] = air_polution["date"].dt.month

#Nulová hypotéza H0: Průměrné hodnoty množství jemných částic jsou pro oba roky stejné.
#Alernativní H1: Průměrné hodnoty množství jemných částic jsou pro oba roky nejsou stejné.
leden_2019 = air_polution[[air_polution["year"] == 2019] and air_polution["month"]== 1]["pm25"]
leden_2020 = air_polution[[air_polution["year"] == 2020] and air_polution["month"]== 1]["pm25"]
leden_2019 = leden_2019.dropna()
leden_2020 = leden_2020.dropna()
print(leden_2019.head())
print(leden_2020.head())
print(mannwhitneyu(leden_2019,leden_2020))
# výsledek: MannwhitneyuResult(statistic=21632.0, pvalue=1.0)
# p-value je 100 a tedy je vyšší než 5% hladina významenosti a tedy nezamítáme nulovou hypotézu - platí, že průměrné hodnoty množství jemných částit jsou pro oba roky stejné.