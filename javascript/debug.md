### Javascript Debug

Als ein Element in der Launch-Configuration:

```
{
    "type": "node",
    "request": "launch",
    "name": "Node",
    "program": "${file}"
    },
```


#### Javascript-Programm ohne HTML 

*Breakpoint setzen, Launch-Configuration wählen, Debug-Modus, Run*

Wenn das Programm einen Dateizugriff macht mit *nodejs*, dann wird im debug-Modus die
Datei aus irgendeinem Grund nicht gefunden. Dann fürs debuggen den relativen Pfad durch
den absoluten Pfad ersetzen.

#### P5JS Javascript

Kann man z.B. damit debuggen. Es öffnet sich dann Chrome. Das funktioniert aber nicht nicht gut

```
{
    "name": "P5JS",
    "type": "chrome",
    "request": "launch",
    "file": "${file}"
},

```


 
