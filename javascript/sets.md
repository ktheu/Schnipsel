### Sets in Javascript


```
let a = [1,2,3,1,2,3]
let s = new Set(a)      // Set { 1, 2, 3 }
for (let x of s) console.log(x)
``` 


#### Menge der verschiedenen Zeichen eines String
 
```
s = new Set("Hallo")   // Set { 'H', 'a', 'l', 'o' }

```
#### Set-Operationen

```
s.add(5)
s.size       // ist Attribut
s.has(2)     // lookup
s.clear()
s.delete(4)
```

#### foreach-Schleife

s.forEach((x) => console.log(x*x))

#### Set in Array umwandeln

```
a = [...s]

```


#### Vereinigung, Schnitt, Differenz

```
function union(setA, setB) {
    var _union = new Set(setA);
    for (var elem of setB) {
        _union.add(elem);
    }
    return _union;
}

```
```
function intersection(setA, setB) {
    var _intersection = new Set();
    for (var elem of setB) {
        if (setA.has(elem)) {
            _intersection.add(elem);
        }
    }
    return _intersection;
}

```

```
function difference(setA, setB) {
    var _difference = new Set(setA);
    for (var elem of setB) {
        _difference.delete(elem);
    }
    return _difference;
}

```
