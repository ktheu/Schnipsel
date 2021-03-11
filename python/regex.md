### Python - Regex

Regular Expressions matchen, suchen und ersetzen Textmuster in Strings.

```
import re
```

[CheatSheet](./regex_cheatsheet.pdf)

Zwei Arten, reguläre Expressions in Python zu definieren:
```
re.compile()
RawString-Notation    (empfohlen)

```

#### Sets und Ranges

Sets und Ranges grenzen den Suchumfang für Textmuster an.

```
[....]  - set: suche nach allem was in dem set ist
[^....] - set: suche nach allem, was nicht in dem set ist
.|.     - entweder oder
(....)  - Gruppe
a-z     - Ranges
A-Z
0-9

```

#### Quantifier
Die Quantifier sind von Hause auf greedy, d.h. sie matchen so viele Zeichen wie möglich
Durch Hinzufügen eines Fragezeichens werden sie non-greedy.

```
*    - 0 oder mehr
+    - 1 mal oder mehr
?    - 0 oder 1 mal
{3}  - genau 3 mahl
{3,} - 3 oder mehr
{3,5} - 3 bis 5 mal

```


#### Anchors
^ hat innerhalb eines Sets eine andere Funktion als außerhalb

```
^   - Anfang eines Strings
$   - Ende eines String
\A  - Anfang eines Strings
\Z  - Ende eines Strings
\b  - Wortgrenze
\B  - keine Wortgrenze

```

#### Groups
Wenn man Gruppen innerhalb des regex Gruppen verwendet, stehen die Resultate via
Matchobjekt über die Funktionen *group* und *groups* zur Verfügung.
 
In group(0) steht der fullmatch, ab Index 1 sind die Matches für die Gruppen zugreifbar
groups() gibt ein Tupel  mit den Inhalten aller Gruppen zurück.

```
(....)   - alles innerhalb der Gruppe = capture group
(?:...)  - alles innerhalb der Gruppe, aber keine capture group
(?#...)  - Kommentar innerhalb der Gruppendeklaration
(..|..)  - entweder oder


```

Benannte Gruppen mit `?P<name>`.  

```
s = '<html><body><h1><h2><span class="mw-headline" id="Entstehung">Entstehung</span></h2></h1></body></html>'
reg = r'<span.*?>(?P<content>.*?)</span>'
mat=re.search(reg,s)
mat.group('content')

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

#### Bestimmte Zeichen aus einem String eliminieren:

```
' '.join(re.findall('[^!.? ]+',test_phrase))

```
#### re-Funktionen

```
re.match()  # matcht am Anfang eines Strings, auch im Multiline-Mode, return Matchobjekt
re.fullmatch()  # matcht den gesamten String, returns Matchobjekt  
re.search()   # sucht innerhalb des Strings, returns Matchobjekt    
re.sub()      # das gematchte Muster wird durch einen anderen String ersetzt und zurückgegeben   
re.subn()     # gibt zusätzlich noch die Anzahl der Änderungen zurück, returns tuple 
re.findAll()  # returns Liste mit gematchten Strings  
re.findIter() # return Iterator, mit dem durch die gefunden matches iteriert werden kann
re.split()    # teilt den String, an dem das Muster matcht, returns Liste

re.match(r'pattern',string,flags=0)
re.sub(r'pattern',repl,string,count=0,flags=0)   # count: max Anzahl Ersetzungen, 0 = unbegrenzt  

```

#### Flags

Mehrere Flags mit dem Pipe-Operator

```
re.IGNORECASE
re.MULTILINE
re.DOTALL      # dot matcht dann auch alle Zeichen der nächstne Zeilen
re.UNICODE     # erweitert \w \W \b \B auf Unicode
re.VERBOSE     # erlaubt Kommentare in dem regulären Ausdruck

```

#### Flag: Verbose
erlaubt  Kommentare in dem regulären Ausdruck

```
reg = r"""\d{2}/\d{2}\s         # 03/02
          \d{2}:\d{2}:\d{2}\s   # 08:51:01
          WARNING(.*)$          # WARNING mit capture group bis Ende
       """  

re.match(reg,x,re.VERBOSE)
```

#### Ersetzungen

```
re.sub(r'ß',r'ss',text)    # ß durch ss ersetzen
re.sub(r'\.',r',',text)    # Punkt durch Komma ersetzen
```

#### Suchen

```
reg = r'\w+essen'       # alle Wörter, die mit essen aufhören
reg = r'<h1>(.*)<\h1>'  # alles, was zwischen einem h1-tag steht
reg = r'\.\S'           # ein Punkt, dem kein Leerzeichen folgt.
mat = re.findall(reg,data)
```

#### String Replacement

```
reg = r'^\\(\w+)\\(\d{4})\\\1\2\.xls'     # \1 ist match der ersten Gruppe, 
                                          # \2 ist match der zweiten Gruppe
```

#### Lookahead and lookbehind

Beim lookahead matcht ein Muster nur dann, wann anschließend ein anderes Muster folgt.
Beim lookbehind matcht ein Muster nur dann, wenn vorher ein anderes Muster war.

```
(?=...)   # positive lookahead
(?!...)   # negative lookahead
(?<=...)  # positive lookbehind
(?<!...)  # negative lookbehind

```

#### Conditionals

Innerhalb einer Gruppe kann ein Muster abgefragt werden (in der Regel auch eine Gruppe)
und dann eine dann-sonst Entscheidung getroffen werden. 

```
(?(1)B|C)

```
wenn Gruppe 1 eine match hat, dann matche Muster B, ansonsten matche Muster C


##### sub und Verbose

Bei re.sub funktioniert der VERBOSE-Modus offenbar nur, wenn der Ausdruck compiled wird und
dort das verbose-Flag gesetzt wird.

```
reg = re.compile(r"""
               \w+
               """,re.X)
```