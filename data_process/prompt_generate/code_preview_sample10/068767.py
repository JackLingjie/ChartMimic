```python
import numpy as np  
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  

# Sample data
x_list = np.linspace(-2.0, 3.5, 1000)
y_list = np.linspace(-2.0, 3.5, 1000)
X, Y = np.meshgrid(x_list, y_list)
Z1 = 2 * X + 3 * Y + 1

# Create a new figure
fig = plt.figure(figsize=(7.0, 5.0))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z1, cmap='viridis')

# Set labels
ax.set_title('Quadratic Approximation 1')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Show the plot
plt.show()
```