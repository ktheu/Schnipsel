## Numpy

[Numpy Tutorial Stanford CS231](http://cs231n.github.io/python-numpy-tutorial/)

### Options 

Die wissenschaftliche Notation wird durch zwei Dezimalstellen ersetzt.
```
np.set_printoptions(precision=2, suppress= True)
np.set_printoptions(formatter={'float': '{: 0.1f}'.format},suppress= True)

```
### 

`np.random.randn()`  erzeugt eine Zufallszahl aus der Normalverteilung mit Mittelwert 0 und Standardabweichung 1.


### Array

```
a = np.arange(100)         # Array von 0 bis 99
np.random.shuffle(a)       # Array mischen (in situ)
a = np.random.randn(5)         # ein Array aus 5 Zufallszahlen, 0-1-normalverteilt 
np.isin(sample, pop)       # sind die Elemente von sample in pop enthalten?

```


### Matrix 

```
a =  np.zeros((3,5),dtype='<U1')      # 3 x 5 matrix mit leeren Strings
a =  np.zeros((3,5),dtype='uint32')   # 3 x 5 matrix mit Nullen
a =  np.random.randn(3,5)             # 3 x 5 Matrix mit Zufallszahlen
a =  np.eye(3)                        # 3 x 3 Einheitsmatrix
a =  np.full((3,5),6)                 # 3 x 5 Matrix mit lauter 6n.
a =  np.full((3,5),' ')                 # 3 x 5 Matrix mit lauter 6n.
```
 
#### Zeilen und Spalten
 
```
a[k,:]        # Zeile k
a[:,k]        # Spalte k
```

#### Sortieren
 
```
a = np.sort(a,axis = 0)        # Spalten sortieren
a = np.sort(a,axis = 0)[::-1]  # Spalten umgekehrt sortieren
a = np.sort(a,axis = 1)        # Zeilen sortieren
 
a = a.transpose()              # Zeilen umgekehrt sortieren
a = np.sort(a,axis = 0)[::-1]
a = a.transpose()

```
 


### Random

`np.random.randn()`  erzeugt eine Zufallszahl aus der Normalverteilung mit Mittelwert 0 und Standardabweichung 1.

```
np.random.randn()        # Zufallszahl aus der Normalverteilung mit Mittelwert 0 und Standardabweichung 1.
np.random.randn(5)       # ein Array aus 5 Elementen

```

Ein Array mischen:
```
a = np.arange(10)
np.random.shuffle(a)
``` 

#### Arange
a = np.arange(100)      # Array von 0 bis 99


### Daten einlesen

Inhalt des Textfiles:


```
XNOR input data
1.0 1.0
1.0 0.0
0.0 1.0
0.0 0.0

```

```
filename = './xnorinput.txt'

with open(filename) as file:
    content = file.readlines()
    # remove first line
    content = content[1:]
    m = np.loadtxt(content)

print(m)

``` 

Ausgabe:

```
[[1. 1.]
 [1. 0.]
 [0. 1.]
 [0. 0.]]

```