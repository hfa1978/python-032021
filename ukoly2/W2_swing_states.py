"""
Swing states
V případě amerických prezidentských voleb obecně platí, že ve většině států dlouhodobě vyhrávají kandidáti jedné strany. Například v Kalifornii vyhrává kandidát Demokratické strany or roku 1992, v Texasu kandidát Republikánské strany od roku 1980, v Kansasu do konce od roku 1968 atd. Státy, kde se vítězné strany střídají, jsou označovány jako "swing states" ("kolísavé státy"). Tvým úkolem je vybrat státy, které lze označit jako swing states.
V souboru 1976-2020-president.csv najdeš historické výsledky amerických prezidentských voleb. Každý řádek souboru obsahuje počet hlasů pro kandidáta dané strany v daném roce.
V souboru jsou důležité následující sloupce:
Year - rok voleb,
State - stát,
party_simplified - zjednodušené označení politické strany,
candidatevotes - počet hlasů pro vybraného kandidáta,
totalvotes - celkový počet odevzdaných hlasů.
"""

import pandas
import requests
import numpy

with requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/1976-2020-president.csv") as r:
  open("1976-2020-president.csv", 'w', encoding="utf-8").write(r.text)
president_elections = pandas.read_csv("1976-2020-president.csv")
#print(president_elections.head())

"""1.Urči pořadí jednotlivých kandidátů v jednotlivých státech a v jednotlivých letech (pomocí metody rank()). Nezapomeň, že data je před použitím metody nutné seřadit a spolu s metodou rank() je nutné použít metodu groupby()."""
president_elections_serazene = president_elections.sort_values(["year", "state", "candidatevotes"])
print(president_elections_serazene[["year", "state", "candidatevotes", "party_simplified", "totalvotes"]])
president_elections_serazene["poradi"] = president_elections_serazene.groupby(["year", "state"])["candidatevotes"].rank(method ="min", ascending=False)
#print(president_elections_serazene[["year", "state", "candidatevotes", "party_simplified", "totalvotes", "poradi"]])

"""2. Pro další analýzu jsou důležití pouze vítězové. Ponech si v tabulce pouze řádky, které obsahují vítěze voleb v jednotlivých letech v jednotlivých státech."""
vitezove = president_elections_serazene[president_elections_serazene["poradi"]==1]
#print(vitezove[["year", "state", "candidatevotes", "party_simplified", "totalvotes", "poradi"]])

"""3. Pomocí metody shift() přidej nový sloupec, abys v jednotlivých řádcích měl(a) po sobě vítězné strany ve dvou po sobě jdoucích letech."""
vitezove["party_simplified_predchozi"] = vitezove["party_simplified"].shift(periods=1)
print(vitezove[["year", "state", "party_simplified", "party_simplified_predchozi"]])

"""4. Porovnej, jestli se ve dvou po sobě jdoucích letech změnila vítězná strana. Můžeš k tomu použít např. funkce numpy.where a vložit hodnotu 0 nebo 1 podle toho, jestli došlo ke změně vítězné strany."""
vitezove["zmena"] = numpy.where(vitezove["party_simplified"] == vitezove["party_simplified_predchozi"],0,1)
#print(vitezove[["year", "state", "party_simplified", "party_simplified_predchozi", "zmena"]])

"""5. Proveď agregaci podle názvu státu a seřaď státy podle počtu změn vítězných stran."""
vitezove_agregace = vitezove.groupby(["state"]).sum("[zmena]")
vitezove_agregace = vitezove_agregace.sort_values(["zmena"], ascending=False)
print(vitezove_agregace)

"""Doplněk 1: U amerických voleb je zajímavý i tzv. margin, tedy rozdíl mezi prvním a druhým kandidátem.
Přidej do tabulky sloupec, který obsahuje absolutní rozdíl mezi vítězem a druhým v pořadí. Nezapomeň, že je k tomu potřeba kompletní dataset, tj. je potřeba tabulku znovu načíst, protože v předchozí části jsme odebrali některé řádky"""
president_elections_serazene["votes_margin_absolute"] = president_elections_serazene["candidatevotes"].shift(periods=1)
#print(president_elections_serazene[["year", "state", "candidatevotes", "votes_margin_absolute", "totalvotes", "poradi"]])

"""Doplněk 2: Můžeš přidat i sloupec s relativním marginem, tj. rozdílem vyděleným počtem hlasů."""
president_elections_serazene["votes_margin_relative"] = (president_elections_serazene["candidatevotes"]-president_elections_serazene["votes_margin_absolute"])/(president_elections_serazene["candidatevotes"]+president_elections_serazene["votes_margin_absolute"])
#print(president_elections_serazene[["year", "state", "candidatevotes", "votes_margin_absolute", "votes_margin_relative", "poradi"]])

"""Doplněk 3: Seřaď tabulku podle velikosti margin (absolutním i relativním) a zjisti, kde byl výsledek voleb nejtěsnější."""
president_elections_serazene_absolute = president_elections_serazene.sort_values(["votes_margin_absolute"])
vitezove2 = president_elections_serazene[president_elections_serazene["poradi"]==1]
vitezove2_absolute = vitezove2.sort_values(["votes_margin_absolute"])
vitezove2_relative = vitezove2.sort_values(["votes_margin_relative"], ascending=False)
print(vitezove2_absolute[["year", "state", "votes_margin_absolute", "votes_margin_relative"]].head())
print(vitezove2_relative[["year", "state", "votes_margin_absolute", "votes_margin_relative"]].head())