## Strings

```
s = 'Hello';
s.length              // Länge
c = s[1]
c = s.charAt(1)
s1 = s.trim()         // blanks löschen
k.toString()          // convert number to String
s.toLowerCase()
s.toUpperCase()
s.replace(',','.');
```

Eine Dezimalzahl mit Komma String in ein Float umwandeln
```
a = parseFloat(a.replace(',','.'));

```
#### Substrings

```
s.slice(start, end)   // end not included
s.slice(start);       // bis zum Ende
```

#### Durch die Zeichen eines Strings iterieren:

```
for (c of s) {
  console.log(c)
}
 
[...s].forEach(c => console.log(c))    # String wird erst in Array verwandelt
```

#### CharCode und Zeichen

```
k = 'a'.charCodeAt()
c = String.fromCharCode(97);
```