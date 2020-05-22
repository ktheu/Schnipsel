## Pandas 

Attributes

```
df.shape
df.size
df.index
df.columns
```

Methods

```
df.head(), df.head(2)
df.tail()
df.info()
df.describe()  # statistische Informationen
df.min()       # Minimum in jeder Spalte
df.mean()
df.mean().sort_values()
df.mean().sort_values().head(2)

```
Optionen
```
pd.options.display.max_rows = 400

```
Spalten selektieren

```
df['age']             # Series-Object
df[['age']]           # ein Dataframe
df[['age','city']]    # mehrere Spalten ergeben ein Dataframe

df.age                # Series-Object
```

Zeilen selektieren
```
df.iloc[0]            # Zeile mit Index 0 selektieren (als Series)
df.iloc[-1]           # letzte Zeile wählen
df.iloc[1:4]          # slicing
df.iloc[[3,12,20]]    # Liste mit Indizes
 
df.iloc[0,4]          # in Zeile 0, Spalte 4 selektieren
df.iloc[:,4]          # Spalte 4