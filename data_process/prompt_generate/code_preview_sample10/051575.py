```python
import matplotlib.pyplot as plt  
import numpy as np  
from mpl_toolkits.mplot3d import Axes3D  
from matplotlib import cm  

u, v = np.mgrid[-10:10:.1, -10:10:.1]  
u = u.T  
v = v.T  

fig = plt.figure(figsize=(7, 5))  
ax = fig.add_subplot(111, projection='3d')  

z = u**2 + v**2  

ax.plot_surface(u, v, z, rstride=8, cstride=8, alpha=0.6)  
ax.contour(u, v, z, zdir='z', offset=-40, cmap=cm.coolwarm)  

ax.set_xlabel('X')  
ax.set_xlim(-10, 10)  
ax.set_ylabel('Y')  
ax.set_ylim(-10, 10)  
ax.set_zlabel('Z')  
ax.set_zlim(-40, 100)  

plt.show()
```