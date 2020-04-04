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