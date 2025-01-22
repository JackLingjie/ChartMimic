```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data for a simple quiver plot example
X, Y = np.meshgrid(np.linspace(-4, 4, 10), np.linspace(-4, 4, 10))
U = -Y
V = X

# Create a figure with the specified size
fig, ax = plt.subplots(figsize=(6.0, 6.0))

# Plot the vector field using quiver
ax.quiver(X, Y, U, V)

# Set title and labels for clarity
ax.set_title('Quiver Plot Example')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Show the plot on screen
plt.show()
```