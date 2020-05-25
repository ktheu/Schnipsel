## Pandas 

Es gibt drei Hauptobjekttypen: Index, Series, Dataframe



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


```
summer = pd.read_csv("summer.csv", index_col="Athlete")  # index labels müssen nicht unique sein
summer.info()
summer[["Metal"]]
summer.loc["Lewis, Car",["Year","Event","Metal"]]
```

## Panda Series

Series und Dataframes haben viele Methoden gemeinsam.

```
ps.to_frame()    # series to dataframe
ps.describe()
ps.count()       # number of nonmissing values
ps.size          #  
ps.dtype         #
ps.sum()         # summiert alle non-missing values, (skipna = True)
sum(ps)          # die Python-Funktion weiß nicht, wie missing values behandelt werden sollen
ps.mean()
ps.std()
ps.min(), ps.max()
ps.unique()      # doppelte werte werden weggeworfen
ps.nunique()     # number of unique elements
ps.value_counts()
ps.value_counts(sort = True, dropna = True, ascending = True, normalize = True)   # normalize gibt relative Häufigkeit zurück
      # der Wert von normalize hängt davon ab, wie dropna gesetzt ist.
ps.value_counts(sort = True, dropna = True, ascending = True, normalize = True , bins = 5)  # 5 halboffene Intervalle 
ps.nlargest(10), ps.nsmallest(n=3)
titanic.age.idxmax()  # returned index des ältesten Passagiers

```

Erstellen von Pandas Series

```
summer["Athlete"]  # nur eine Spalte eines Dataframes wählen
summer.iloc[0]     # nur eine Zeile eines Dataframes wählen
pd.read_csv("summer.csv", usecols = ["Athlete"], squeeze = True)   # eine Spalte mit squeeze einlesen
pd.Series([3,4,5,6])
pd.Series([3,4,5,6], index = ["a","b","c","d"], name = "Sales")
pd.Series(np.array([3,4,5,6]))
pd.Series({1:'a',2:'b'}) 
```

rows in Series mit einem RangeIndex sollte man immer mit loc oder iloc selektieren, nicht mit der reinen Klammer

### Sortieren von Series
```
df.sort_index(ascending = True)   # erzeugt copy
df.sort_index(inplace = True)     # sortiert in situ
df.sort_values()
df.sort_values(na_position = "last")
```

### Manipulating Data in Series
sales["Sun"] = 0           # ein Element - alle Duplikate werden überschrieben
sales.iloc[3] = 14         # ein Element - auch der Wert in dem originalen dataframe wird geändert !
sales = (sales / 1.1).round(2)     # vectorisierte Operation

## Pandas Index Object

In vielen Fällen ist des nützlich ein label-based Index zu haben, um label-based selektieren zu ermöglichen.
Der Index ist immutable, d.h. direkte Updates auf ein Element sind nicht möglich.

```
summer.index, summer.columns  sind Index-Objects
pd.Index([1,2,3])
pd.Index(['a','b','c'],name='Zeichen')
pd.Index(range(1,4))
pd.reset_index()  # der index-column wird durch range-index ersetzt, der bisherige label-index wird normale Spalte
pd.index = aList        # wenn die Anzahlen stimmen geht das
pd.index.name = "Name"  # Namen des Index kann man setzen
pd.columns = aList      # die Anzahl müssen stimmen
```

summer.rename(index = {"a":"new"},inplace=True)
summer.rename(columns = {"a":"anew", "b":"bnew"},inplace=True)

## Filter DataFrames

```
titanic[titanic.sex == 'male']           # square-bracket notation not recommended
titanic[titanic.sex == 'male']['fare']   # chained indexing not recommended
titanic.loc[titanic.sex == 'male']             # loc-notation recommended
titanic.loc[titanic.sex == 'male', 'fare']     # loc-notation recommended

mask = titanic.dtypes == 'object'
titanic.loc[:,~mask]  # alle Spalten, die keine Objekte sind, d.h. alle numerischen Spalten
mask1 & mask2, mask1 | mask2

summer.loc[summer.YEAR >= 1992]
summer.loc[summer.YEAR.between(1960,1969,inclusive=True)]
summer.loc[summer.YEAR.isin([1972,1996])]

(titanic.age == 80).any()      # checked ob einer in der series 80 ist
all(), 
titanic.fare.all()             # prüft auf 0

```

### Spalten entfernen

```
summer.drop(columns = ['Sport','Discipline'],inplace = True)     # oder
summer.drop(labels = "Event", axis = "columns", inplace = True)  # oder
del summer["Event"]   # not recommended
```


### Zeilen entfernen

```
summer.drop(index = ['HAJOS, ALFRED'], inplace = True)  # oder 
summer.drop(labels = "HAJOS, ALFRED", axis = "index", inplace = True)   
summer = summer.loc[~(mask1|mask2),inplace = 'True']
```

### Spalte hinzufügen

```
titanic["Zeroes"] = 0    # 
titanic["New"] = "a"
titanic["YearOfBirth"] = 1912 - titanic.age  # vectorized operation
titanic.fare = titanic.fare*10
titanic.Ones = 1      #  Ein Attribut wird erzeugt, aber keine Spalte

relatives = titanic.sipsp + titanic.parch
titanic.insert(loc=6, column='relatives', value = relatives)
```

### Dataframes von Scratch erzeugen.

Wenn die Daten spaltenweise als Listen vorliegen, mit Listennamen als gewünschte Spaltennamen
dann:

```
dic = {'col1':col1, 'col2':col2}
df = pd.DataFrame(dict)
df.set_index(col1)
```

Wenn die Daten zeilenweise als Listen vorliegen

```
df = pd.DataFrame([row1, row2], index = ['row1', 'row2'], columns = ['col1', 'col2'])

```

Eine einzelne Zeile hinzügen
```
players.loc[5,:] = [ ,  ,  , ]   # die Dimension muss stimmen  
df.loc['Rest'] = 2000
```