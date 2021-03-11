## Bitmasks

Um sich für indizierte Dinge zu merken, ob eine Eigenschaft vorhanden ist oder nicht, eignen sich
Bitmasks. 

```
def testBit(int_type, offset):
    mask = 1 << offset
    return(int_type & mask)

# setBit() returns an integer with the bit at 'offset' set to 1.

def setBit(int_type, offset):
    mask = 1 << offset
    return(int_type | mask)

# clearBit() returns an integer with the bit at 'offset' cleared.

def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return(int_type & mask)

# toggleBit() returns an integer with the bit at 'offset' inverted, 0 -> 1 and 1 -> 0.

def toggleBit(int_type, offset):
    mask = 1 << offset
    return(int_type ^ mask)
```

Beispiel: (hier entspricht die Variable mask der obigen Variablen int_type)



```
mask = 0
mask = mask | 1 << 0 | 1 << 2 | 1 << 5          #  es werden die Bits 0,2,5 auf 1 gesetzt

for i in range(8):                              # range(int(math.log2(mask)))
    if (mask & 1 << i):
        print(i)                   #  0,2,5

mask =  mask ^ 1 << 2                           # toggle bit an stelle 2
```