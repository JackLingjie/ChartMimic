```python
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  
import numpy as np  

# Sample data
x, y, z = np.meshgrid(np.arange(-5, 5, 1), np.arange(-5, 5, 1), np.arange(-5, 5, 1))
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z))

# Create a new figure
fig = plt.figure(figsize=(5.0, 5.0))
ax = fig.add_subplot(111, projection='3d')

# Plot the quiver
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
```