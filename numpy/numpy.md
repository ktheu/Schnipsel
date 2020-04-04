## Numpy

[Numpy Tutorial Stanford CS231](http://cs231n.github.io/python-numpy-tutorial/)

### 

`np.random.randn()`  erzeugt eine Zufallszahl aus der Normalverteilung mit Mittelwert 0 und Standardabweichung 1.


### Array

```
a = np.arange(100)         # Array von 0 bis 99
np.random.shuffle(a)       # Array mischen (in situ)
a = np.random.randn(5)         # ein Array aus 5 Zufallszahlen, 0-1-normalverteilt 

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