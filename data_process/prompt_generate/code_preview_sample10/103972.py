```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data for quiver plot
x = np.linspace(0, 2 * np.pi, 10)
y = np.linspace(0, 2 * np.pi, 10)
X, Y = np.meshgrid(x, y)
U = np.cos(X)
V = np.sin(Y)

# Create a new figure
plt.figure(figsize=(6.0, 6.0))
plt.title("Quiver Plot Example")

# Plot the vector field using quiver
plt.quiver(X, Y, U, V)

# Show the plot
plt.show()
```