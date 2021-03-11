## C++

#### Allgemeines

```
sizeof(p)   # zeigt die Größe der Variable im Speicher an in bytes

```

```
double x = 3.13;   // schublade heißt x und kann eine double speichern
sizeof(x)          // die größe der schublade ist 8 byte
&x                 // die schublade steht an dieser speicheradresse 
double* p;         // schublade heißt p und kann einen pointer für eine double speichern
p = &x;            // in die schublade p wird die adresse der schublade x geschrieben
*p                 // der Inhalt, der an der Adresse steht, die in  p gespeichert ist ( 3.14)

```
#### Vectoren  [doc](https://en.cppreference.com/w/cpp/container/vector)

```
#include <vector>
#include <algorithm>
#include <numeric>

```


```
vector<int> state(4,0);    // Vektor mit 4 Werten, mit 0 initialisiert
state[2];
state.at(2);               // exception, wenn index ungültig
state.push_back(24);       // Wert inten anhängen
state.pop_back();
state.size();
```

```
fill(a.begin(), a.end(), 3);   // überalll 3   -  in algorithm
iota(a.begin(), a.end(), 3);   // beginnt bei 3 und dann immer eins drauf  - in numeric


```

```
bool my_sort(int& i, int& j) return i<j;
sort(a.begin(), a.end(), my_sort)

```
```
for (int i = 0; i < state.size(); ++i) {
  cout << state[i] << ' ';
}
```


2D-Vector (Matrix) erstellen und initialisieren
```
int rows = 3;
int cols = 2;

vector<vector<int>> matrix(rows, vector<int>(cols, 0));   // eine rows x cols Matrix mit 0 initialisieren
for (int i = 0; i < matrix.size();++i) {

  for (int j = 0; j < matrix[i].size(); ++j) {
    cout << matrix[i][j] << " ";
  }
  cout << endl;
}

```

#### Arrays

Mit std::array
```
#include <array>

using std::array;
using std::get;

int main() {
    array<array<int, 4>, 4> casts = { { {1,0,0,0},{0,1,0,0},{0,0,1,0},{0,0,0,1} } };
    array<int, 4> goal = { 0,0,0,9 };
    array<int, 4> startstate = { 0,0,0,0 };
    array<int, 4> teststate = { 0,-2,0,0 };

    cout << "Ausgabe: " << valid(teststate) << endl;
    return 0;
}

bool valid(array<int,4> state) {
    int summe = 0;
    for (int i = 0; i < state.size(); i++) {
        summe += state[i];
        if (state.at(i) < 0) return false;
    }
    return summe <= 10;
}

```

oder :
Immer wenn eine Array an eine Funktion übergeben wird, muss die Länge mitübergeben.
Die Variable, die ein Array benennt, zeigt auf das erste Array-Element. Sie enthält keine
Information über die Länge des Arrays.

```
// bool valid(int state[], int sz) {       äquivalent
bool valid(int* state , int sz) {
    int summe = 0;
    for (int i = 0; i < sz; i++) {
        summe += state[i];
        if (state[i] < 0) return false;
    }
    return summe <= 10;
}


int main() {
  int casts[4][4] =  { {1,0,0,0},{0,1,0,0},{0,0,1,0},{0,0,0,1} } ;
  int goal[4] = { 0,0,0,9 };
  int startstate[] = { 0,0,0,0 };
  int teststate[] = { 0,-2,0,0 };

	cout << "Ausgabe: " << valid(teststate,4) << endl;
	return 0;
 
}
```



