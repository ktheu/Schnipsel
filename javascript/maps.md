### Javascript Maps

_[doc](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Map)_


The keys of objects can only be of the string type. In Maps, keys can be of any value.


Eine Map aus einem Array von Arrays machen:

```
const a = [
  ['a', 1],
  ['b', 2],
  ['c', 3],
  ['d', 3],
  ['e', 4],
]
let m = new Map(a);

let a = [...m]     //    aus einer Map ein Array von Arrays machen

``` 

Mit den geschweiften Klammern macht man ein Objekt, keine Map. Beim Objekt sind die keys immer Strings.

```
let m = {6:27, 14:19}  // =>      { '6': 27, '14': 19 }  

let a = [[6,27], [14,19]]
let m1 = new Map(a)    // =>  Map { 6 => 27, 14 => 19 }  

```


Übliche Operationen auf Maps

```
let m = new Map();
 
if (m.has(k)) ...     // ist k Schlüssel in m?
m.set(k,v);           // setzen eines key-value Paares
let v = m.get(k);     // undefined, falls k nicht vorhanden
m.size                // size of map ist Attribut
m.delete(k)           // delete entry
m.clear()             // alle entries löschen

```

#### Loops

Loop mit destructuring assignment:

```
for (let [k, v] of m) {
  console.log(`${k} - ${v}`);
}

// oder 

for (let [k, v] of m.entries()) {
  console.log(`${k} - ${v}`);
}
```

Alle Schlüssel durchlaufen:

```
for(let k of m.keys()) ...   
```


#### Maps zusammenführen
Die Maps m1 und m2 werden erst in Arrays verwandelt, die dann beide 
dem Konstruktor von Map übergeben werden.

```
let m = new Map([...m1],[...m2]) 
```


#### Reversed Map 
value wird zu key und umgekehrt (wenn das gehts)

```
let m1 = new Map([...m].map(([k,v]) => [v,k]))
```

#### Aus einer Liste eine Map machen, die beide Richtungen enthält
```
let a = [[6,27], [14,19]];
let a1 = [...a].map(([k,v]) => [v,k])
let m = new Map([...a, ...a1]) 
```