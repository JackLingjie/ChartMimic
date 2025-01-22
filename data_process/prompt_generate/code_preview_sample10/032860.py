```python
import matplotlib.pyplot as plt  
import numpy as np  

# Create a grid of points
x, y = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.25))

# Calculate the function values
z = x * np.exp(-x**2 - y**2)

# Calculate the gradients
v, u = np.gradient(z, 0.2, 0.2)

# Create a new figure
fig, ax = plt.subplots(figsize=(6.0, 4.0))

# Plot the quiver
ax.quiver(x, y, u, v, color="yellow")

# Set title
plt.title('Quiver Plot', fontsize=15)

# Show the plot
plt.show()
```