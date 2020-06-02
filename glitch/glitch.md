## Glitch

### Allgemeines

server.js wird immer wieder automatisch gestartet. Deswegen ist es wichtig, dass am Ende ein
*listen* steht. Sonst ist es wie eine Loop. Console.logs in server.js erscheint im Log (auf Glitch)


### nedb-Datenbank anlegen und füllen

Daten in eine nedb-Datenbank schreiben. Ohne das listen würden permanent Daten in die Datenbank geschrieben werden. Das Verzeichnis und das file brauchen vorher nicht angelegt zu werden.

```
const Datastore = require('nedb');  

const db = new Datastore(".data/highscore.db");
db.loadDatabase();     // nicht vergessen !

let users = [{name: 'N.N.1', score: 0}, {name: 'N.N.2', score:0}, {name: 'N.N.3', score:0}]

db.insert(users, function(err, docs) {
     docs.forEach(function(d) {
         console.log('Saved user:', d.name);
     });
 });

app.listen(process.env.PORT);
```

### Inhalt der nedb-Datenbank ansehen und ändern

```
Terminal 
cd .data
vi highscore.db  

Edit: H nach oben links, 20dd - 20 Zeilen löschen

 + -Edit
:wq

```
Nur Ansehen mit `cat highscore.db`


