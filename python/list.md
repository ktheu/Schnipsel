## Python - List


```
len(a)
min(a)
max(a)

```

```
x = a.index(max(a))   # argmax
```

#### Mit zwei versetzen Schleifen durch eine Liste laufen
```
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        print(a[j]-a[i],end = ' ')
    print()
```
oder so:
```
for i, x in enumerate(a[:-1]):
    for y in a[i+1:]:
        print(y-x,end=' ')
    print()   
```