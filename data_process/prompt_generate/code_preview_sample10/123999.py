```python
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  
import numpy as np  
  
# Sample data for 3D plot
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
x, y = np.meshgrid(x, y)
z = x**2 + y**2  

# Create a new figure
fig = plt.figure(figsize=(7.0, 5.0))  
ax = fig.add_subplot(111, projection='3d')  
  
# Plot the surface
ax.plot_surface(x, y, z, cmap='viridis')  
  
# Set labels
ax.set_xlabel('X-axis')  
ax.set_ylabel('Y-axis')  
ax.set_zlabel('Z-axis (Cost)')  
  
# Show the plot
plt.show()
```