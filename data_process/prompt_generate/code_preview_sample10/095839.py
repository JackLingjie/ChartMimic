```python
import matplotlib.pyplot as plt  
import numpy as np  
from matplotlib.colors import ListedColormap  
from sklearn import datasets  
from sklearn.neighbors import KNeighborsClassifier  

# Load iris dataset  
iris = datasets.load_iris()  
X_train = iris["data"][:-10, :2]  
y_train = iris["target"][:-10]  

# Parameters  
n_neighbors = 10  
h = 0.02  

# Color maps  
cmap_light = ListedColormap(["#DC143C", "#0000FF", "#32CD32"])  
cmap_bold = ListedColormap(["#FF1493", "#000080", "#008000"])  

# Create classifier  
clf = KNeighborsClassifier(n_neighbors=n_neighbors, weights="uniform")  
clf.fit(X_train, y_train)  

# Define plot boundaries  
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1  
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1  

# Create meshgrid  
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))  

# Predict  
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])  
Z = Z.reshape(xx.shape)  

# Plot  
plt.figure(figsize=(7.0, 5.0))  
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)  
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cmap_bold, edgecolors='k', s=20)  
plt.xlim(xx.min(), xx.max())  
plt.ylim(yy.min(), yy.max())  
plt.title("3-class classification (k={}, weight={})".format(n_neighbors, "uniform"))  

plt.show()
```