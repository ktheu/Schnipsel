## Graphen

Modellierung eines gerichteten Graphen.

```
// G0 ist ein Objekt  
G0 = {
  'a': new Set('bc'),
  'b': new Set('d'),
  'c': new Set('bd'),
  'd': new Set('b')
}

// G ist eine Map
const G = new Map(Object.entries(G0));

// alle Nachbarn von a
console.log(G.get('a'))

// gibt es Kante von a nach b   ?
console.log(G.get('a').has('b'))


// alle Knoten von G durchlaufen:
for (let [k,v] of G) {
  console.log(k);
}
```

Eine Graphen mit den Knoten a b c d e mit leeren Sets initialisieren

```
let s = 'abcde';
let a = s.split('');
let b = a.map(x => [x,new Set()]);
let G = new Map(b)
 
```

Durch die keys in sortierter Reihenfolge laufen

```
for (x of [...G.keys()].sort()) {
  console.log(x)
}
```