```python
import matplotlib.pyplot as plt  
import numpy as np  
from mpl_toolkits.mplot3d import Axes3D  

x_list = np.linspace(-2.0, 3.5, 1000)  
y_list = np.linspace(-2.0, 3.5, 1000)  
X, Y = np.meshgrid(x_list, y_list)  

Z1 = 2 * X + 3 * Y + 1  

fig = plt.figure(figsize=(7.0, 7.0))  
ax = fig.add_subplot(111, projection='3d')  

ax.plot_surface(X, Y, Z1, cmap='viridis')  
ax.set_title('3D Surface Plot')  
ax.set_xlabel('x')  
ax.set_ylabel('y')  
ax.set_zlabel('z')  

plt.show()
```