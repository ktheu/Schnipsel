## NEDB

[doc](https://github.com/louischatriot/nedb/)

#### Datenbank anlegen

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


```

#### Datensätze aus Datenbank löschen

```
db.remove(query, options, callback)
```

Alle Datensätze löschen
```
db.remove({}, { multi: true });  
 
// oder

db.remove({ }, { multi: true }, function (err, numRemoved) {
   console.log('Number of records removed', numRemoved)
});

```

#### Datensätze zählen

db.count({}, function(err, count) {
    console.log(count);
});  
```


