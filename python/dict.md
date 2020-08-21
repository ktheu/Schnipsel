## Python dictionaries

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

#### Einen zufälligen Schlüssel wählen
import random
k = random.sample(m.keys(), 1)[0]
