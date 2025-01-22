```python
import numpy as np  
import matplotlib.pyplot as plt  

# Create data  
y, x = np.mgrid[10:-10:100j, 10:-10:100j]  
x_obstacle, y_obstacle = 0.0, 0.0  
alpha_obstacle, a_obstacle, b_obstacle = 1.0, 1e3, 2e3  

p = -alpha_obstacle * np.exp(-((x - x_obstacle)**2 / a_obstacle + (y - y_obstacle)**2 / b_obstacle))  
dy, dx = np.gradient(p, np.diff(y[:2, 0])[0], np.diff(x[0, :2])[0])  

# Plot  
fig, ax = plt.subplots(figsize=(7.0, 5.0))  
im = ax.imshow(p, extent=[x.min(), x.max(), y.min(), y.max()], cmap=plt.get_cmap('plasma'))  
ax.quiver(x[::10, ::10], y[::10, ::10], dx[::10, ::10], dy[::10, ::10])  

# Add colorbar  
cax = fig.add_axes([0.85, 0.1, 0.05, 0.8])  
fig.colorbar(im, cax=cax, orientation='vertical')  
ax.set(aspect=1, title='Quiver Plot')  

# Show the plot  
plt.show()
```