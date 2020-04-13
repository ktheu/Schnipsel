### Python - Regex

```
import re
```


#### Die Indizes aller Vorkommen eines patterns

```
s = "nababana dfasdfna dwernaana 999"
b = [(m.start(0), m.end(0)) for m in re.finditer("na", s)]
print(b)

Ausgabe:  [(0, 2), (6, 8), (15, 17), (22, 24), (25, 27)]
```


#### Die Indizes aller Vorkommen von Zeichenfolgen, die nur aus Buchstaben bestehen und mindestens Länge 4 haben

```
regex = r'[a-zA-ZüäöÜÄÖß]{4,}'
for m in re.finditer(regex,text):
    i ,j = m.start(0), m.end(0)
    print(i,j)

```