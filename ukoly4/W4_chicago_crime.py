import pandas
from sqlalchemy import create_engine, inspect

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "info"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "KCTiqURc=juzddI0"
engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)

#Chicago Crime
#Tabulka crime v naší databázi obsahuje informace o kriminalitě v Chicagu. Data si můžete i interaktivně prohlédnout na mapě zde.
#Dataset je poměrně velký, a tak si určitě vytáhneme vždy jen nějaký výběr, se kterým budeme dále pracovat.
#1. Pomocí SQL dotazu si připrav tabulku o krádeži motorových vozidel (sloupec PRIMARY_DESCRIPTION by měl mít hodnotu "MOTOR VEHICLE THEFT").
crime = pandas.read_sql("crime", con=engine)
kradez = pandas.read_sql("SELECT * FROM crime WHERE \"PRIMARY_DESCRIPTION\" = 'MOTOR VEHICLE THEFT'", con=engine)
#kradez = crime[crime["PRIMARY_DESCRIPTION"]=="MOTOR VEHICLE THEFT"]
#print(kradez)

#2. Tabulku dále pomocí pandasu vyfiltruj tak, aby obsahovala jen informace o krádeži aut (hodnota "AUTOMOBILE" ve sloupci SECONDARY_DESCRIPTION).
kradez_aut = kradez[kradez["SECONDARY_DESCRIPTION"]=="AUTOMOBILE"]
print(kradez_aut)

#3. Ve kterém měsíci dochází nejčastěji ke krádeži auta?
kradez_aut["datum"] = pandas.to_datetime(kradez_aut["DATE_OF_OCCURRENCE"])
kradez_aut["mesic"] = pandas.to_datetime(kradez_aut["datum"]).dt.month
#print(kradez_aut[["SECONDARY_DESCRIPTION","DATE_OF_OCCURRENCE","datum","mesic"]])
print(kradez_aut.groupby(["mesic"]).size().sort_values())
#K nejvíce kráděžím aut dochází v září.