## Statistics

#### Imports
```
from scipy.stats import zscore
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from statsmodels.formula.api import ols, gls

```



```
pop.mean()
np.mean(pop)
np.median(pop)

```

Der Median bei gerader Anzahl von Elementen (z.B. 50) wird wie folgt berechnet:
```
(sample[24] + sample[25]) / 2

```

#### Normalisieren

```
dfn = df.apply(zscore)

# oder

dfn = StandardScaler().fit_transform(df)
```

#### Principal Components

```
dfn = df.apply(zscore)
pca = PCA(n_components=2)
pc = pca.fit_transform(dfn)
dfpc = pd.DataFrame(data = pc, columns=["PC1", "PC2"])
pca.explained_variance_ratio_
```

#### Linear Regression

```

```