## Matplotlib

[doc](https://matplotlib.org/contents.html)  [axis-doc](https://matplotlib.org/api/axes_api.html)


#### Übliche Imports

```
import matplotlib.pyplot as plt
%matplotlib inline

```

#### Zwei Plots nebeneinandern

```
# zwei plots nebeneinander
x = [1, 2, 3, 4]
y1 =  [1, 4, 2, 3]
y2 =  [3, 1, 4, 2]

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
plt.suptitle("Zwei Plots", size=16)
ax1 = plt.subplot(1, 2, 1)
plt.plot(x,y1)               # line-plot
#plt.scatter(x,y1)           # scatter-plot
#plt.bar(x,y1)               # bar-plot
ax2 = plt.subplot(1, 2, 2)
plt.plot(x,y2)  

ax1.set_xlabel('xlabel1')
ax2.set_xlabel('xlabel2')
ax1.set_title('title1')
ax2.set_title('title2')
plt.show()
```

#### Zwei Plots nebeneinander mit Gridspec

```
import matplotlib.gridspec as gridspec
plt.figure(figsize=(10, 4))
plt.suptitle("Zwei Plots", size=16)
G = gridspec.GridSpec(1, 2)
ax1 = plt.subplot(G[0,0])
plt.scatter(x,y1)
ax2 = plt.subplot(G[0,1])
plt.scatter(x,y2)

ax1.set_xlabel('xlabel 1')
ax2.set_xlabel('xlabel 2')
ax1.set_title('title1')
ax2.set_title('title2')
plt.show()
```

#### Zwei Plots nebeneinander mit seaborn
```
import seaborn as sns
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
plt.suptitle("Zwei Plots nebeneinander", size=16)

ax1 = plt.subplot(1, 2, 1)
sns.lineplot(x=x, y=y1, color='r', ax=ax1)
# sns.barplot(x=x, y=y1, color='r', ax=ax1)
# sns.scatterplot(x=x, y=y1, color='r', ax=ax1)

ax2 = plt.subplot(1, 2, 2)
sns.lineplot(x=x, y=y2, color='b', ax=ax2)   

ax1.legend(['alpha'], facecolor='w')
ax1.set_xlabel('xlabel 1')
ax2.set_xlabel('xlabel 2')
ax1.set_title('title1')
ax2.set_title('title2')
plt.show()
```


Sollen die Plots übereinandergelegt werden, dann einfach die zweite plt.subplot-Anweisung weglassen.


#### Viele Plots (14 x 3)

```
fig, axs = plt.subplots(14, 3, figsize=(20, 40))
for i in range(1,43):
    sns.lineplot(x=dfY.index, y=dfY.iloc[:,i], color='r', ax=plt.subplot(14, 3, i))
```