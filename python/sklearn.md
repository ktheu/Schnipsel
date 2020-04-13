## Sklearn

#### Datasets

```
import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets

```

Koordinaten (x0,x1) erzeugen, y sind zufällige Labels 0/1.
```
X, y = sklearn.datasets.make_moons(20,noise=0.2)
plt.scatter(X[:,0],X[:,1],s=40,c=y,cmap=plt.cm.Spectral)
```