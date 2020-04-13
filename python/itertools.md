### Python - Itertools

```
from itertools import *

```
#### Kombinationen

Die Elemente aller Teilmengen der Länge 2 aufzählen:


```
a = [3, 4, 7, 9]
for x,y in combinations(a,2):
    print(x,y)
```

Alle Kombinationen der Länge 3 aus den Zahlen 1-5

```
for x in itertools.combinations(range(1,6),3):
    print(x)
```