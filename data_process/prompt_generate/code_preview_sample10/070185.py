```python
import numpy as np  
import matplotlib.pyplot as plt  

delta = 0.025  
x = y = np.arange(-3.0, 3.0, delta)  
X, Y = np.meshgrid(x, y)  
Z1 = np.exp(-((X**2) + (Y**2)))  
Z2 = np.exp(-((X-1)**2 + (Y-1)**2))  
Z = Z2 - Z1  

x = X.ravel()  
y = Y.ravel()  
z = Z.ravel()  

xcond = (-1 < x) & (x < 1)  
ycond = (-2 < y) & (y < 0)  
cond = xcond & ycond  
xnew = x[cond]  
ynew = y[cond]  
znew = z[cond]  
for i in range(20):  
    x = np.hstack((x, xnew))  
    y = np.hstack((y, ynew))  
    z = np.hstack((z, znew))  

xmin = x.min()  
xmax = x.max()  
ymin = y.min()  
ymax = y.max()  

gridsize = 30  

plt.figure(figsize=(7.0, 5.0))  
plt.hexbin(x, y, C=z, gridsize=gridsize, cmap=plt.cm.RdBu, vmax=abs(z).max(), vmin=-abs(z).max())  
plt.axis([xmin, xmax, ymin, ymax])  
cb = plt.colorbar()  
cb.set_label('Mean Value')  

plt.show()
```