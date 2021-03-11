## Kernels hinzufügen und löschen

kernels für jupyter-notebooks sind in 
`c:\Users\khthe\AppData\Roaming\jupyter\kernels\`

```
python -m ipykernel install --user --name=nlp_course
jupyter kernelspec uninstall powershell
jupyter kernelspec list

```


## JupyterLab


Bilder nicht mit einem relativen Pfad `./` referenzieren, sondern z.B. in denselben Ordner legen oder einen
Unterordner der dann so angegeben wird. `<img src="img/bild.png" />`. Denn Abschluss-Slash nicht vergessen.

```
Tab  - autocomplete 
Shift-Tab - docString
Shift-Enter - ausführen und neue Zelle
Shift-Strg  - ausführen und in Zelle bleiben
Fn-einfg - zum Verlassen des Überschreibemodus (einfg = 0 auf Nummern)

```

## JupyterNotebook

```
Shift-Tab - docString
Shift-2xTab - docString mit Parameter
Shift-3xTab - doc Fenster bleibt 10sec an
Shift-4xTab - getrenntes doc-Fenster
```

## Conda

```
!conda env list   # das aktive env hat einen *
!conda list       # installierte Pakete zeigen

conda env create -f nlp_course_env.yml

```
## HTML ausführen

```
from IPython.display import display, HTML
display(HTML('<h1>Hello World</h1>'))
```

## Breite der Ausgabe
Hängt im wesentlichen von der Komponente, ab die die Ausgabe macht.

```
pd.set_option('display.width', 1000)   # Pandas

```

## Pandas DataFrame ausgeben, wie wenn df als letzte Anweisung steht
```
from IPython.display import display, HTML
display(HTML(df.to_html()))
```

## speichert anything in das entsprechende file
```
%%writefile something.py
anything

```

### wo befindet sich das Notebook ?
```
pwd
```

## Binder (nbviewer)

An die URL dranhängen zum Refresh:
```
?flush_cache=true   
```