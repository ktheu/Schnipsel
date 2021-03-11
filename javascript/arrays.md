## Arrays


_[doc](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Global_Objects/Array)_

 
```
const a = [1,2];
a = new Array(5).fill(0);   // Länge 5, mit 0 initialisiert
a.push(4);                  // am Ende was anhängen
a.pop();                    // am Ende was löschen
a.unshift(7);               // am Anfang was anhängen
a.shift();                  // am Anfang was löschen
a.includes(2);              // ist 2 enthalten ?
b = a.map(x => 2*x)         // alle Elemente des Arrays ändern
b = a.slice()               // copy
b = [...a]                  // copy mit Spread-Operator
[x1, x2] = a;               // destructuring, wenn a zwei Elemente enthält
a.length                    // Länge des Arrays
```

Durch ein Array laufen

```
a = [1,2,3]
for (let i = 0; i < a.length; i++) {
  console.log(a[i]);
}
 
a.forEach(function(x) {
  console.log(x);
});

a.forEach(x => console.log(x));

for (let x of a) {
  console.log(x);
}
```

#### Elemente aus dem Array löschen

`splice` verändert das Array, mit `filter` kann man ein neues Array erzeugen

```
splice(start,laenge)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];    # a wird verändert
b = a.splice(2,3);                     # b enthält den gesplicten teil
```


Wenn man den Wert des zu löschenden Elements kennt: Index bestimmen und dann mit splice löschen.
```
let a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
let idx = a.indexOf(5)
for( let i = 0; i < a.length; i++){
  if ( a[i] === 5) { a.splice(i, 1); }
}
```

Mit filter geht das viel einfacher
```
let a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
a = a.filter(x => x !== 5)                         # Die 5 aus a herausnehmen.
```

const a = [17, 16, 18, 19, 21, 17];
const b = a.filter( x => x > 18 );

#### Shuffle Array nach Fisher-Yates
 
```
for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * i)
    const temp = a[i]
    a[i] = a[j]
    a[j] = temp
}

```

#### Array sortieren

```
s = 'afasdfa';
a = s.split('');
a.sort();              # inplace
a.sort().reverse();    # umgekehrt sortieren
```

#### Einige übliche Operationen

```
sum = array.reduce((pv, cv) => pv + cv, 0);        # Die Summe bilden
min = state.reduce((pv, cv) => Math.min(pv,cv));   # Das Minimum in einem Array finden
```