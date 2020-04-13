### Python - Dateizugriff

#### Dateien öffnen

Einfaches öffnen einer Datei
```
f = open('./beispieldaten/twist1.txt')
```

Datei zum lesen/schreiben öffnen
```
f = open(indata,"r",encoding='utf-8')
f = open(outdata,"w",encoding='utf-8')
```

#### Einlesen von zwei Zahlen, die in einer Zeile stehen

```
x, y = [int(k) for k in f.readline().split()]
```
oder so:
```
x, y = map(int, f.readline().split())
```

#### n Zahlen in eine Liste einlesen, eine Zeile pro Zahl

```
a = [int(f.readline()) for i in range(n)]
```


#### Die Zeilen als String einlesen, ohne den Zeilenumbruch:
```
lines = [x.rstrip('\n') for x in f.readlines()]
```

#### eine unbekannte Anzahl von Zahlen einlesen, eine Zahl pro Zeile

a = [int(x.rstrip('\n')) for x in f.readlines()]

#### Zahlen in eine Liste einlesen und noch was hinzufügen
```
a = [0, *map(int, input().split()), w]   # oder
a = [0] + map(int, input().split()) + [w]
```