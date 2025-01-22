```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a new figure
fig = plt.figure(figsize=(7.0, 7.0))
ax = fig.add_subplot(111, projection='3d')

# Get points for a mesh grid
u, v = np.mgrid[0:2*np.pi:200j, 0:np.pi:100j]

# Setting x, y, z coordinates
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)

# Plotting the wireframe
ax.plot_wireframe(x, y, z, rstride=5, cstride=5, linewidth=1)

# Show the plot
plt.show()
```