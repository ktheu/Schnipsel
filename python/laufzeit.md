## Laufzeitmessung


### walltime

In Jupyter Notebook als erste Anweisung in einer Zelle
```
%%time

```

### perf_counter

```
import time
zeit = 0

start = time.perf_counter()
# code to track here             # <--- update hier
# in defs ggf:
# global zeit
end = time.perf_counter()
zeit = zeit + end-start


print("Laufzeit in Sekunden: ",round(zeit,4))
```

### Line_Profiler

Im Jupyter Notebook:
```
%load_ext line_profiler
```

Die Funktion, um die es geht, in ein getrenntes File speichern.

```
%%writefile something.py
def sometest():
    z = 0
    for i in range(10):
        z+=i
    return z
```

```
from something import sometest
%lprun -T ausgabe.txt -f sometest sometest()
```