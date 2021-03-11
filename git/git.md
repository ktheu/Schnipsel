### Git  




VSCode als Editor nutzen
```
$ git config --global core.editor "code --wait"
```

### Sonstiges
```
$ git branch -d name   # delete brach
$ git checkout -b name  # neuen branch erstellen mit checkout
$ git commit -am 'msg'  # alles stagen und committen
```

### Git-UseCases

#### Auf 2 PCs abwechselnd am gleichen Code in Directory D arbeiten.

1. Mit Explorer nach D gehen, rechte Maustaste, Git Bash Here
2. $git init, $git commit -am 'initial commit'
3. Auf GitHub ein Repo anlegen: RD und http-url kopieren.
4. $git remote add origin url, git push -u origin master



#### Ein lokales und remote Repo wieder auf den Zustand des initial commit setzen

Bsp. initial commit = 8ec0, im lokalen repo:

```
$ git reset 8ec0 --hard
$ git push -f 
```

### Github Pages

Wenn eine Seite über Github-Pages erreicht werden soll, muss sie in dem branch gh-pages stehen.
gh-pages sollte dann der default page sein und master sollte man am besten löschen

### Eine neue GitHub-Page erstellen für Ordner jwinf

1. Mit VSCode in den Ordner gehen jwinf gehen, Terminal erzeugen, git init

2. .gitignore mit geeignetem Inhalt anlegen
3. commit inital (in vscode) Damit ist branch master erstellt

4. git branch gh-pages
5. git checkout gh-pages
6. git branch -d master

---- Auf Github

7. Auf Github das Repository ktheu/jwinf erstellen

---- Im Terminal

8. git remote add origin https://github.com/ktheu/jwinf.git
9. In VScode pushen, da kommt dann: ... hat kein upstream .. wollen sie publishen? - Ja

Die _config.yml Datei sollte da (glaube ich) nicht dabei sein, die ist
nur in dem ursprünglichen githubio-repo.