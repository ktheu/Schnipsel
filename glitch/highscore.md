## Muster für Highscore Spiel in Glitch

### server.js

```
const express = require("express");
const app = express();
const path = require("path");
const bodyParser = require("body-parser");
const Datastore = require("nedb");

const db = new Datastore(".data/highscore.db");
db.loadDatabase(); // nicht vergessen !

// remove all records from database

// db.remove({}, { multi: true }, function(err, numRemoved) {
//   console.log("Number of records removed", numRemoved);
// });

const highscoreAnz = 5;
let users = [];

for (let i = 0; i < highscoreAnz; i++) {
  users.push({ name: "N.N", score: 0 });
}

db.count({}, function(err, count) {
  if (count === 0) {
    db.insert(users, function(err, docs) {
      docs.forEach(function(d) {
        console.log("Saved user:", d.name);
      });
    });
  }
});

app.use(bodyParser.json());

app.get("/", (req, res, next) => {
  res.sendFile(path.join(__dirname, "./", "views/index.html"));
});

app.get("/highscore", (req, res, next) => {
  db.find({})
    .sort({
      score: -1 // Nach score absteigend sortieren
    })
    .exec(function(err, docs) {
      if (err) console.log(err);
      if (docs.length > highscoreAnz) {
        for (let i = highscoreAnz; i < docs.length; i++) {
          db.remove({ _id: docs[i]._id });
        }
        docs = docs.slice(0, highscoreAnz);
      }
      res.json(docs);
    });
});

app.post("/highscore", (req, res, next) => {
  db.insert(req.body);
  res.redirect("/");
});

app.listen(process.env.PORT);

```


### views/index.html

```

<html>
  <head>
    <title>Highscore-Demo</title>
    <meta charset="utf-8" />
    <style>
      html,
      body {
        margin: 0;
        padding: 0;
        background-color: #1a1a1a;
        padding-top: 100px;
      }
      canvas {
        display: block;
        margin: auto;
      }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.9.0/p5.js"></script>
    <script>
      let hsmin = -1;
      let highscoreText = "";
      let state = "WELCOME";

      // set in init0
      let score;
      let name;

      function preload() {
        getHighscore();
      }

      function setup() {
        createCanvas(300, 300);
        noStroke();
        init0();
      }

      function draw() {
        background(100);
        switch (state) {
          case "WELCOME":
            welcome();
            break;
          case "PLAY":
            play();
            break;
          case "GAMEOVER":
            gameover();
            break;
          case "HIGHSCORE":
            highscore();
            break;
          case "NEWHIGHSCORE":
            newhighscore();
            break;
          case "WAIT":
            wait();
            break;
        }
      }

      function init0() {
        score = 0;
        name = "";
      }

      function welcome() {
        textAlign(CENTER, CENTER);
        textSize(14);
        text("WELCOME to GAME", 0, 30, width);
        text(highscoreText, 0, 60, width);
        let regeln =
          "Press ENTER to start";
        text(regeln, 0, 200, width);
      }

      function gameover() {
        if (score > hsmin) {
          state = "HIGHSCORE";
        }
        else {
          text(highscoreText, 0, 60, width);
          text("Your Score: " + score, 0, 200, width);
          text("Press r to restart", 0, 260, width);
        }
      }

      function play() {
        score = int(random(1000));
        fill(0);
        textSize(30);
        textAlign(CENTER, CENTER);
        text(score, 0, 100, width);
        textSize(14);
        text("Hit space to stop",0,260,width);
      }

      function highscore() {
        text(highscoreText, 0, 60, width);
        text("Your Score: " + score, 0, 200, width);
        text("Your Name: " + name, 0, 230, width);
      }

      function newhighscore() {
        text(highscoreText, 0, 60, width);
        text("Press r to restart", 0, 260, width);
      }

      function wait() {
        text(highscoreText, 0, 60, width);
        text("Your Score: " + score, 0, 200, width);
        text("Your Name: " + name, 0, 230, width);
        text("... updating database", 0, 260, width);
      }

      function getHighscore() {
        httpGet(
          "/highscore",
          "json",
          false,
          function(res) {
            highscoreText = "Highscore:\n\n";
            for (let i = 0; i < res.length; i++) {
              highscoreText += res[i].name + ": " + res[i].score + "\n";
            }
            hsmin = res[res.length - 1].score;
          },
          function(err) {
            console.log(err);
          }
        );
      }


      function keyTyped() {
        if (state === "HIGHSCORE") {
          name += key;
        }
      }

      function keyPressed() {
        if (state === "WELCOME") {
          if (keyCode === ENTER) {
            state = "PLAY";
          }
        }

        if (state === "PLAY") {
          if (key === ' ') {
            state = "GAMEOVER";
          }
        }

      if (state === "GAMEOVER") {
        if (key === 'r') {
          init0();
          state = 'PLAY';
        }
      }

        if (state === "HIGHSCORE") {
          if (keyCode === BACKSPACE) name = name.substr(0, name.length - 1);
          if (keyCode === ENTER) {
            state = "WAIT";
            httpPost("/highscore", { name: name, score: score }, function(res) {
              getHighscore();
              state = "NEWHIGHSCORE";
            });
          }
        }

        if (state === "NEWHIGHSCORE") {
          if (key === "r") {
            init0();
            state = "PLAY";
          }
        }
      }
    </script>
  </head>

  <body></body>
</html>


```