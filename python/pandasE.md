## Pandas Essentials


```
df.drop_duplicates(inplace = True)      # doppelte Datensätze löschen


# Gruppieren   
dfg = df.groupby('name').CPC.count().sort_values(ascending=False) 
dfg = df.groupby('Tag').agg(Menge = ("Menge","sum"), Anzahl = ("Menge", "count"))   


# Zeilen selektieren
df.loc[df.nummer==472]               

# Spalte, Index renamen
df.rename(index = {0:"Zeile0"},inplace=True)
df.rename(columns = {"0":"Spalte0", "1":"Spalte1"},inplace=True)

# alle Spalten renamen (Listenlänge muss passen)
df.columns = ['Tag','Art','Bemerkung','Betrag']
```