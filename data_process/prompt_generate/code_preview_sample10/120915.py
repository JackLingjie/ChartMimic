```python
import numpy as np
import matplotlib.pyplot as plt

# Generate two 1-D arrays: u, v
u = np.linspace(-2, 2, 41)
v = np.linspace(-1, 1, 21)

# Generate 2-D arrays from u and v: X, Y
X, Y = np.meshgrid(u, v)

# Compute Z based on X and Y
Z = np.sin(3 * np.sqrt(X**2 + Y**2))

# Create a filled contour plot with a color map of 'viridis'
plt.figure(figsize=(6.0, 4.0))
plt.contourf(X,Y,Z,cmap='viridis')
plt.colorbar()
plt.title('Filled Contour Plot')

# Show the plot
plt.show()
```