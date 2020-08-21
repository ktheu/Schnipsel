### Sys 


#### Aufruf

```
c:\Users\khthe\Anaconda3\python.exe filesUI.py

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