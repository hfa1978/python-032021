"""V souboru jsou data o délce zrn pšenice v milimetrech pro dvě odrůdy - Rosa a Canadian. Proveď statistický test hypotézy o tom, zda se délka těchto dvou zrn liší. K testu použij Mann–Whitney U test, který jsme používali na lekci.
V komentáři u programu formuluj hypotézy, které budeš ověřovat. Je potřeba formulovat dvě hypotézy - nulovou a alternativní. Provádíme oboustranný test, takže alternativní hypotézy by měla být, že průměry délky zrna jsou různé (nejsou si rovné).
Pomocí modulu scipy urči p-hodnotu testu a porovnej ji s hladinou významnosti 5 %. V komentáři uveď závěr, jestli nulovou hypotézu na základě p-hodnoty zamítáme.
Platí pravidlo, že je-li p-hodnota menší než hladina významnosti, nulovou hypotézu zamítáme. V opačném případě říkáme, že ji nezamítáme.
Měl(a) bys dospět k p-hodnotě menší než 1 %."""

import pandas
from scipy.stats import mannwhitneyu
import requests

r =  requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/psenice.csv")
open("psenice.csv", 'w', encoding="utf-8").write(r.text)
data = pandas.read_csv("psenice.csv")
#print(data)

# nulová hypotéza H0: průměrná délka zrna pšenice pro odrůdy Rosa a Canadian jsou stejné
# alternativní hypotéza H1: průměrná délka zrca pšenice odrůdy Rosa a Canadian není stejná

rosa = data[["Rosa"]]
canadian = data[["Canadian"]]
print(mannwhitneyu(rosa, canadian))
#print(mannwhitneyu(data[["Rosa"]], data[["Canadian"]]) - alternativní zápis

#výsledek: MannwhitneyuResult(statistic=array([4884.5]), pvalue=array([3.52243752e-24]))
#p-value je 0,00000000000000000000000352243752000 a tedy menší než hladina významnosti 5% a tedy nulovou hodnotu zamítáme; platí tedy že průměrná délka zrna není stejná

