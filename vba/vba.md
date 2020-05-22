## VBA

__[CheetSheet](./VBAcard2.pdf)__

__[Tutorial](https://www.vba-tutorial.de/editor/)__

VBA-Code versteckt sich immer bei einer Wirtsanwendung, also muss man erst eine Wirtsanwendung öffnen (z.B. Excel) um
an den Code-Editor zu kommen. 

Beim Speichern eines Dokuments, das VBA-Code enthält, muss man einen speziellen Dateityp wählen: Datei mit Makros, z.B: xlsm

`Alt-F11`  Öffnen des VBA-Editors
`Fn+Einfg`  Überschreibemodus ein/aus

Im `Direktfenster` kann man unmittelbar Code eingeben oder fertigen Code aufrufen. 


Mit `Enter` kann man Code im Direktfenster direkt ausführen
```
Debug.Print "Hallo Welt!";  
```

Unter `Ansicht` sollte man die Symbolleiste `Bearbeiten` dauerhaft einblenden.

### Module

Um Programmcode zu speichern erstellen wir Module. Jedes Modul wird in einem eigenen Codefenster angezeigt.

#### Module erstellen
Im Programmfenster ein Objekt markieren, erstellen, Modul


#### Sub-Prozeduren
Module können Sub-Prozeduren enthalten. Im Direktfenster kann die Sub-Prozedur mit `Hallo` aufgerufen werden.
Für den Namen gilt: VBA berücksichtigt Groß-/Kleinschreibung nicht, behält jedoch die Schreibweise bei, mit der der Name deklariert wurde.

```
Sub Hallo()
    Debug.Print ("Hallo Welt");
End Sub

```


#### Funktions
Eine Function-Prozedur unterscheidet sich kaum von einer Sub. Allerdings kann eine Function auch einen Rückgabewert haben.
Dem Namen der Function wird im Rumpf der Rückgabewert zugewiesen. Eine selbst geschriebene Function verhält sich genau wie eine in VBA integrierte Funktion.

Der Rückgabewert einer Function hat, genau wie eine Variable, einen Datentyp, der stets definiert werden sollte. Ansonsten hätte die Funktion den (selten empfehlenswerten) Datentyp Variant. Der Datentyp wird hinter den Klammern angegeben. Im Gegensatz dazu hat eine Sub natürlich keinen Datentyp - mangels Rückgabewert.

In einem Excel-Feld wird die Funktion dann mit Ich() aufgerufen.
```
Function Ich() As String
    Ich = "Hallo Ich"
End Function

```

Wir können den Functions Argumente übergeben
```
Function Bruttopreis(Netto As Currency) As Currency
    Bruttopreis = Netto * 1.19
End Function

Function Kombi(LF_Deu As String, LF_Eng As String, LF_Mat As String, LF_Ges As String)
    Kombi = 1
    
End Function

```




#### Verschiedenes


```
Zeilenkommentare  -  einfaches Hochkomma
Fortsetzungszeichen  -  Unterstrich
Nothing - der Nullwert, wie null oder none

``` 

#### Variablen

`Option Explicit` -  vor Gebrauch muss eine Variable deklariert werden
`Dim`   - Variablendeklaration

```
Dim i, j
Dim s As String
Dim i As Integer
Dim x As Double
Dim x As Variant    // Typ kann variieren
Const pi = 3.1415   // Konstanten
```


#### Enum
```
Enum Farbe
    Karo = 9
    Herz = 10
    Pik = 11
    Kreuz = 12
    Grand = 24
End Enum
```

#### Eigene Datentypen
```
Type Koordinate
    x As Long
    y As Long
End Type

Dim p As Koordinate

p.x = 800
p.y = 600
```


#### Arrays

Angegeben wird der letzte gültige Index, beginnend bei 0. Wochentag hat also 7 Elemente.

```
Dim Wochentag(6) As String
Dim Brett(7, 7) As String

Dim Feld() As Long     # Wenn die Anzahl noch nicht feststeht
Dim Anzahl As Byte
Anzahl = 3
ReDim Feld(Anzahl)     # Bei ReDim wird schon vorhandendes gelöscht
```

#### Strings
```
&             Verkettung
Like          mit Platzhalter * und #  (beliebig viele / ein Zeichen)
```

#### Lebensdauer und Sichtbarkeit

 
Modul1:
```
Option Explicit
Private modulweit As Boolean
Public ueberall As Boolean

Sub meineSub()
    Dim nurHier As Boolean
    
    nurHier = True
    modulweit = True
    ueberall = True
End Sub

```

Modul2:
```
Option Explicit
Public Const MwSt = 0.19
Private Const Modul = "Modul2"

Sub VariablenTest()
    nurHier = True   'Fehler
    modulweit = True 'Fehler
    ueberall = True
End Sub
```

#### Static

Obwohl x und y den gleichen Datentyp haben, wird x bei jedem Aufruf von mehr jeweils um 1 erhöht, y bekommt dagegen immer wieder aufs Neue 1 zugewiesen. x hat also eine längere Lebensdauer als y.
```
Sub mehr()
    Static x As Long
    Dim y As Long
    
    x = x + 1
    y = y + 1
    Debug.Print "x: " & x & " y: " & y
End Sub
```