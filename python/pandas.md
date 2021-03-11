# Pandas 

Es gibt drei Hauptobjekttypen: Index, Series, Dataframe

*Dataframe*:  eine zweidimensionale Datenstruktur bei denen die Zeilen und Spalten gelabelt sind
(index, columns) und bei denen die Spalten möglicherweise unterschiedliche Typen halten.

*Series*: ein eindimensionales gelabeltes Array, das jeden Datentyp enthalten kann. Es ist ähnlich wie ein dict, nur mit
viel mehr Möglichkeiten. Wichtige Unterschiede: der Index hat eine wählbare Reihenfolge und ist nicht notwendig eindeutig.

### Optionen
```
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
```

## Series [doc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html)

 

### Series erstellen
Eine Series bekommt man auch, wenn man von einem dataframe eine Spalte selektiert oder nur eine Zeile.
Achtung: wenn man dann einen Wert in einem solchen Series ändert, ändert sich auch der Wert in dem originalen
Dataframe, deswegen erhält man eine Warnung.

```
summer["Athlete"]
summer.Athlete
summer.iloc[0]
pd.read_csv("summer.csv", usecols = ["Athlete"], squeeze = True)   # ohne squeeze wirds dataframe
```

```
s = pd.Series(np.random.randint(10, 20, size=100))     # erhält range-Index
s = pd.Series([3, -5, 7, 4],  index=['a',  'b',  'c',  'd'])  
s = pd.Series([4,5,2,7])     # erhält range-Index, geht auch mit tuple und np.arrays
```

### Series vs dicts

```
m = {'a':3, 'b':-5, 'c':7, 'd':4}  
s = pd.Series([3, -5, 7, 4],  index=['a',  'b',  'c',  'd'])   
s.to_dict()    # ergibt m
pd.Series(m)   # ergibt s

# Entsprechungen der dict und Series-Operationen
m['a'] = 4   -   s['a'] = 4
m['e'] = 5   -   s['e'] = 5
m.keys()     -   s.index
m.values()   -   s.values 
m.items()    -   s.items()
'b' in m     -   'b' in s
len(m)       -   s.size, len(s)
```

### Dict-Comprehensions vs. Series-Operationen

```
m = {'a':3, 'b':-5, 'c':7, 'd':4}  
s = pd.Series([3, -5, 7, 4],  index=['a',  'b',  'c',  'd'])   
m1 = {k : 2*v for k, v in m.items()}     -  s1 = s * 2
m1 = {2*k : v for k, v in m.items()}     -  s1 = s.copy(); s1.index = s.index.map(lambda x : 2*x)
m2 = {k : v  for k, v in m.items() if v > 0}  -  s2 = s[s>0]
m2 = {k : v for k,v in m.items() if k >'b'}     -  s2 = s[s.index>'b']
```

### Series: Schleifen 
```
for x in s:
   print(x)             # geht durch die values !

for x in s.index:
   print(x)             # geht durch die keys
```

### Series: Attribute und Methoden

```
s = pd.Series([3,-5, 7, 4, 4, 3],  index = range(6))
s.dtype      #   zeigt Datentyp der values
s.head(), s.tail()
s.shape, s.size, len(s)
s.count()    #   Number of non-missing values
s.unique()   #   Liste mit den verschiedenen values
s.nunique()  #   Anzahl der verschiedenen values
s.max(), s.min(), s.mean(), s.median(), s.std()  # bezieht sich alles auf die values
s.sum()      #   Summe aller non-missing values   
s.describe()
s.name = 'value'      # Name der value-Spalte (wird bei Umwandlung in dataframe übernommen)
s.index.name = 'key'  # Name der index-Spalte (wird bei Umwandlung in dataframe übernommen)
s.drop_duplicates(inplace = True)       # doppelte löschen
s.rank(ascending=False)  # erstellt eine Rangordnung der Werte 
s.rank(ascending=False, method = "min").sort_values(ascending = True)  # method bezieht sich auf die Behandlung gleicher Ränge
df = s.to_frame()     # Konversion in ein dataframe
```

```
s.value_counts()                    # returns series mit den value_counts
s.value_counts(normalize = True)    # returns series mit relativen Häufigkeiten
s.value_counts(sort = True, dropna = True)
s.value_counts(bins = 5)            # der Wertebereich wird in 5 gleiche große bins aufgeteilt

s.nlargest(4), s.nsmallest(3)
s1 = s.sort_values(inplace = False, ascending=True, ignore_index=False)    # defaults
k = s.argmax()                   # Position des größten values
k = s.idxmax()                   # Index des größten values 
argmin(), idxmin()
```

### Series: indexing and slicing

rows in Series mit einem RangeIndex sollte man immer mit loc oder iloc selektieren, nicht mit der reinen Klammer.
Bei der Klammer weiß man nicht, ob man position-based indexing oder label-based indexing macht (iloc or loc)

```
age = pd.read_csv("titanic.csv", usecols = ["age"], squeeze=True)
age[-1]       geht nicht
age.iloc[-1]  geht
age.iloc[:3]  # bei index-based slicing ist der bis-Wert excluded
age.loc[:3]   # bei label-based slicing ist der bis-Wert included
age.loc[[4, 6]]   # mehrere index-labels wählen
```

### Series sortieren
Man kann nach den values oder nach dem index sortieren
```
m = {1:10, 3:25, 2:6, 4:36, 5:2, 6:0, 7:None}
s = pd.Series(m)
s1 = s.sort_index()
s.sort_index(ascending = True, inplace= True)
s1 = s.sort_values(na_position = 'last')
```

### Series: Daten ändern
Vektorisierte Operationen
```
s = s/1.1
s = s.round(3)
s = s.str.lower()
s = s.str.split()
s = s.str.contains('x')
df = df[df.c1.str.contains('x)]           # alle Zeilen mit 'x' in c1 enthalten 
df = s.str.split(" ",n=1,expand = True)   # neue Spalte
```

```
s = s.apply(lambda x: str(x) + '1')   # alle Werte ändern
```

## Index-Objects - [doc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.html?highlight=index#pandas.Index)
Sehen aus wie Listen, können aber mehr. Index Objekte sind immutable
```
s.index, s.columns
s.axes            # zeigt beide Index-Objekte
s.columns.tolist()
s.index.is_unique()
s.index.get_loc('label')    
```

### Index erstellen

```
r = pd.Index(range(1,4))
r = pd.Index(['Mo','Di','Mi'], name = 'Tag')
s = pd.Series([10,11,12], index = r)
```

### Index: change row-Index
In vielen Fällen ist es nützlich ein label-based Index zu haben, um label-based selektieren zu ermöglichen.
```
summer = pd.read_csv("summer.csv", index_col="Athlete")     # beim import index bestimmen
summer.reset_index()   # erhält range-index, bisherigen index wird column
summer.reset_index(drop = True, inplace = True)   # bisheriger index wird ersetzt
summer.set_index('Year', drop = True)        # Year wird neuer Index und verschwindet als column
summer.index.name = 'Medal' 
```

### Index: change column-Labels
```
df.columns
df.columns.name = 'Spalten'
df.columns = ['Tag','Art','Bemerkung','Betrag']     #   Listenlänge muss passen
```

### Index: rename
```
df.index[0] = 'x'   # geht nicht, da index-Objekte immutable sind
df.rename(index = {0:"Zeile0"},inplace=True)
df.rename(columns = {"0":"Spalte0", "1":"Spalte1"},inplace=True)
```

## Dataframes - [doc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

### Dataframe erstellen 

df.c1 ist attribute notation, 
df['c1'] ist square bracket notation

Dataframe mit Spalten c1, c2 und Index-Spalte idx
```
df = pd.DataFrame()
df['c1'] = [10,20,20,20,30]
df['c2'] = [100,200,300,400,500]
df.index.name = 'idx'  
df.columns.name = 'cols'
```

Die Daten liegen als Liste von Zeilen vor.
```
df = pd.DataFrame([[0, 1],[2,3]], index = ['r1', 'r2'], columns = ['c1', 'c2'])
```

Die Daten liegen als dictionary mit den Spalten als values vor
```
df = pd.DataFrame({'c1':col1, 'c2':col2})
```

```
df = pd.DataFrame(np.eye(5),dtype = 'int')
df = pd.DataFrame(np.zeros((2,3)))
df = pd.DataFrame(np.arange(5*7).reshape((5,7)))

```
### Dataframe: Methoden und Attribute

```
df.shape, df.size, df.index, df.columns
df.head(), df.head(2), df.tail()
df.info()
df.describe()  # statistische Informationen
df.min(), df.mean()      # Minimum, Mean jeder Spalte
df.mean().sort_values()
df.mean().sort_values().head(2)
df.nunique()     # number of unique values in each column in order of appearance
df.c1.unique()   # die verschiedenen werte der Spalte c1 als np-array
```

### Dataframe: Sortieren

```
df.sort_values(by=['c1', 'c2'], ascending = [False, True])  # default: inplace = False
df.sort_values(by= 'c1', ignore_index = True) # der range-Index wird neu aufgebaut und nicht mitsortiert      
 
df.nlargest(n=5, columns = 'c1')    
df.nsmallest(n=5,columns = 'c2')   

df["c2"] = df.c1.rank(ascending = False, method="min")  # ein Rang-Spalte c2 für die Werte in c1  # method bezieht sich auf die
                                                        # Behandlung gleicher Werte
```

### Doppelte Datensätze
```
df.drop_duplicates(inplace = True)  # doppelte Datensätze rausschmeissen
df = df.drop_duplicates()   # doppelte Datensätze rausschmeissen
df = df[~df.duplicated()]   # oder so 
```


### Dataframe: Spalten selektieren
```
df['c1']             # ein Series-Object
df[['c1']]           # ein Dataframe
df[['c1','c2']]      # mehrere Spalten ergeben ein Dataframe
df.c1                # Series-Object
```

### Dataframe: Zeilen selektieren 
iloc geht über die Index-Position
```
df.iloc[0]            # Zeile mit Index 0 selektieren (als Series)
df.iloc[-1]           # letzte Zeile wählen
df.iloc[1:4]          # slicing
df.iloc[[3,12,20]]    # Liste mit Indizes
 
df.iloc[0,4]          # in Zeile 0, Spalte 4 selektieren
df.iloc[:,4]          # Spalte 4
```

loc macht label-Positioning
```
df[df.c1 == 'x']           # square-bracket notation not recommended
df.loc[df.c1 == 'x']       # loc-notation recommended
df.loc[df.c1 == 'x', 'c2'] # Spalte c2 aus allen zeilen mit x in Spalte c1
df[df.c1 == 'x'][c2]       # chained indexing, result wie oben, not recommended
```

### Dataframe: Filter Beispiele
Mit loc kann man Zeilen (1.Argument) und Spalten (2.Argument) selektieren. 

Alle Zeilen, bei denen die Spalte c1 mit 'x' beginnt
```
df.loc[df.c1.str.startswith('x')]    # alle Zeilen, die in c1 mit x beginnen

sel = df.c1.str.contains('x1|x2')    # alle Zeilen, in denen in c1 ein x1 oder x2 vorkommt 
df.loc[sel]

mask = df.dtypes == 'object'
df.loc[:,~mask]  # alle Spalten, die keine Objekte sind, d.h. alle numerischen Spalten
# mask1 & mask2, mask1 | mask2

df.loc[mask1 & mask2, ['c1','c2']]  # mask1,2 selektieren Zeilen, c1, c2 die Spalten
df.loc[mask1 | mask2, ['c1','c2']]  # mask1,2 selektieren Zeilen, c1, c2 die Spalten

df.loc[df.year >= 1992]
df.loc[df.year.between(1960,1969,inclusive=True)]
df.loc[df.year.isin([1972,1996])]
df.loc[(df.year >= start) & (df.year <= end)]    # die Klammern braucht man, weil & stärker bindet
```
 
### Dataframe: Checks
 
```
(df.c1 == 80).any()     # checked ob ein Wert in c1 80 ist
(df.c1 == 80).all()     # checked ob ein Wert in c1 80 ist
df.c1.all()             # prüft auf nicht gleich 0
```

### Zeilen und Spalten renamen

```
df.rename(index = {0:"Zeile0"},inplace=True)
df.rename(columns = {"0":"Spalte0", "1":"Spalte1"},inplace=True)

```
### Spalten umordnen:

```
cols = df.columns.tolist()
order = [7,5,0,1,2,3,4,6,8]
cols_new = [cols[i] for i in order]
df.reindex(columns=cols_new)

```

Spalte mit Index 5 nach vorne holen:
```
cols = df.columns.tolist()
order = list(range(len(cols)))
order.pop(5)
order.insert(0,5) 
cols = [cols[i] for i in order]
df.reindex()

```
### Spalten entfernen und hinzufügen

```
df.drop(columns = ['c1','c2'],inplace = True)    # Spalten löschen
df.drop('c1',axis = 1)                           # oder so
df['c3'] = 0  
df.insert(loc=1,column = 'c3', value=17)
df.insert(loc=1,column = 'c4', value=df.c1+df.c2 )
df1.reindex(columns = df.columns)                # die Reihenfolge der Spalten in df1 wie in df 
```

### Zeilen entfernen und hinzufügen

```
df.drop(index = 'r1', inplace = True)   
df.drop(index = ['r1','r2'], inplace = True)
 
mask1 = df.c1.str.startswith('x')   # alle zeilen löschen, bei denen Spalte c1 mit x beginnt.
df.loc[~mask1,inplace = 'True']
df.loc[~(mask1 | mask2)]

df.loc[5,:] = [ ,  ,  , ]   # die Dimension muss stimmen
df.loc[5] = 10              # alle Spalten werden mit 10 gefüllt
df = df.append(df1, ignore_index = True)   # ein gleichartiges df hinzufügen
```

### Gruppieren   
```
dfg = df.groupby('c1').c2.count().sort_values(ascending=False) 
dfg = df.groupby('c1').agg(newname1 = ("c2","sum"), newname2 = ("c2", "count"))  #  relabeling   
df['cneu'] = df.groupby('c1').c2.transform('mean')   #  eine neue Spalte mit dem gruppenspezifischen mean.
```

### Stack und Unstack

unstack ändert den shape des df von long-format zu wide-format. stack macht das Gegenteil

```
df.unstack()                           # der innerste Index-Level wird in Spalten umgewandelt
df.unstack(level = -2, fill_value = 0)  # bei einem doppelten Index wird der äußere in columns gewandelt

```
### Dataframe: Indexing und Slicing

Regel:
*wenn man das DataFrame verändern will: vermeide chained indexing*, also nutze nur loc oder iloc und nicht
die square-brackets notation.
*wenn man slices eines DataFrames verändern will, ohne das ursprüngliche DataFrame zu verändern: .copy()*

```
df.loc[1:3]  # bis is included
df.iloc[1:3] # bis is not included
s = df.iloc[:10,'c1'].copy()        # Spalte c1, die ersten 10 Einträge

df.c1[1] = 41             # update, chained indexing: not recommended
df.loc[1,'c1'] = 41       # update with loc: is recommended
df.iloc[1,3] = 41         # geht auch mit index-positioning

s = df.loc[:9,'c1'].copy()   # Aus Spalte c1 die ersten 10 Einträge (bei range-index)

```
 

### Summary Statistics

```
axis:  0 = 'index', 1 = 'columns'
df.describe()
df.count(axis = 'index')  #  anzahl der not Nan in jeder spalte # (calculate along the index) 
df.mean(axis = 'index')
df.sum(axis = 'index')
df.cumsum(axis = 'index')
df.corr()
df.c1.corr(df.c2)  # Korrelation zwischen 2 columns
df.agg(['mean', 'std'])
df.agg({'c1':'mean','c2':['min','max']})
```



### apply, map, applymap

apply geht auf df oder series

```
def myfunc(series):
    return series.max() - series.min()
df.apply(myfunc, axis = 0)   # myfunc bekommt jeweils die column-series als argument und gibt einen Wert zurück

df.apply(lambda x: x.max() - x.min())   # dasselbe mit lambda, axis=0 ist default

def myfunc(series):
    return reduce(lambda x,y: x+y, series)
df.groupby('c1').c2.apply(my_func)    # wenn die series 1-D np.arrays sind, werden die elementweise aufsummiert

df.apply.c1(lambda x : str(x) + '1')     # alle Elemente der Spalte c1 verändern
df.applymap(lambda x: 0.4*x-5)           # jedes Element des df ändern
df * 0.4 - 5                             # ginge hier auch

```

### multiindex

Mit einem Multiindex führt man quasi eine weitere Dimension ein: index1, index2, column

```
df.set_index(['c1','c2'])
df.sort_index(ascending = [True, False])  
df.swaplevel()            # switched die reihenfolge der indizes
df.reset_index()          # wieder zum eindimensionalen Rangeindex zurück
df.loc[(1,'x'),c3]        # drei Index-Levels bei 2 Indizes
df.loc[([1,2],['x1,x2')),:]  
df.loc[(slice(None),slice('x1')), :]   # allgemeinste Form
```


### Plots

```
titanic.plot()
titanic.plot(subplots = True, figsize=(15,12), sharex = False)
titanic.age.plot(figsize=(12,8), fontsize=13, c='red', linestyle=':', xlim = (200,400), ylim = (20,40))
titanic.age.plot(figsize=(12,8), fontsize=13, xticks = range())
plt.title('Titanic - Ages', fontsize = 15)
plt.legend(loc='best', fontsize = 15)
plt.xlabel('PassengerNo', fontsize = 13)
plt.ylabel('Age', fontsize = 13)
plt.grid()
plt.style.use("seaborn")
plt.show()

```

plt.style.available  # list mit verfügbaren styles

### Pickle
dataframes mit pickle saven und laden

```
df =  pd.read_pickle('data.pkl')
df.to_pickle('data.pkl')

```
andere Objekte mit pickle saven und laden

```
import pickle
pickle.dump(aList, open("data.pkl", "wb")) 
aList = pd.read_pickle('data.pkl')
```