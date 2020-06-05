## Python

[Installationen](./installation.md)

[Itertools](./itertools.md)

[Dateizugriff](./dateizugriff.md)

[Regex](./regex.md)

[List](./list.md)

[Dictionaries](./dict.md)

[NLP](./nlp.md)

[Pandas](./pandas.md)


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