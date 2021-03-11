## Strings

f-Strings - [doc](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

```
name = 'Fred'
print(f'His name is {name}.')

print(f'His name is {name!r}')    # mit Hochkommata bei Fred

print(f'{name}:{10}')             # Minimum-Länge 10
print(f'{name}:.>{10}')           # rechtsbündig mit . als Padding

print(f'k = {k:.0f})              # ohne Dezimalstelle
print(f'x = {x:.4f})              # mit 4 Dezimalstellen
 
``` 

Man kann auch die [strftime](https://strftime.org/)-Kürzel in den
f-Strings verwenden

```
from datetime import datetime
today = datetime(year=2018, month=1, day=27)
print(f'{today:%B %d, %Y}')
```

### Methoden

```
s.count('a')   # Anzahl Vorkommen
```