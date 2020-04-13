## Python

[Installationen](./installation.md)

[Itertools](./itertools.md)

[Dateizugriff](./dateizugriff.md)

[Regex](./regex.md)

[List](./list.md)







### Listen

#### Mit zwei versetzen Schleifen durch eine Liste laufen
```
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        print(a[j]-a[i],end = ' ')
    print()
```
oder so:
```
for i, x in enumerate(a[:-1]):
    for y in a[i+1:]:
        print(y-x,end=' ')
    print()   
```

### Dictionaries

#### In einem dict abspeichern, wie häufig Werte in einer Liste vorkommen
```
m = {}
for x in a:
    if x in m:
        m[x]+=1
    else:
        m[x]=1
```
oder so:
```
m = {}
for x in a:
    m[x] = m.get(x,0) + 1
```
oder mit der Klasse Counter _[doc](https://docs.python.org/3.8/library/collections.html#collections.Counter)_

```
from collections import Counter
m = Counter(a)
# m = dict(Counter(a))
```

#### Module OS
```
import os
print(os.getcwd())   # listet das current working directory

```

#### import von einem anderen Verzeichnis

```
A - 
  B -
    C
    c.py
mytools -
  __init__.py
  tool.py
```
In c.py möchte man tool.py importieren. Dazu in mytools eine leere __init__.py anlegen. 
```python
import sys
sys.path.insert(0, '../../mytools/')
from mytools import tool
```