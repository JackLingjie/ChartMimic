```python
import matplotlib.pyplot as plt  
import numpy as np  

XLIM = (-4, 4)  
YLIM = (-4, 4)  

fig = plt.figure(figsize=(6.0, 6.0))  
ax = plt.axes(xlim=XLIM, ylim=YLIM)  
ax.set_aspect('equal')  

ax.hlines(0, *XLIM, lw=0.5)  
ax.vlines(0, *YLIM, lw=0.5)  

x = np.linspace(*XLIM, 21)  
y = np.linspace(*YLIM, 21)  
X, Y = np.meshgrid(x, y)  

def f(x, y):  
    return x + y**2  

norm = np.hypot(1, f(X, Y))  

kwargs = {'angles':'xy', 'width':0.002, 'pivot':'mid'}  
ax.quiver(X, Y, 1/norm, f(X, Y)/norm, **kwargs)  

plt.show()
```