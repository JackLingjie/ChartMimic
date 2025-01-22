```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
x = np.linspace(0, 1, 50)
y = np.linspace(0, 1, 50)
xv, yv = np.meshgrid(x, y, indexing='ij')
Bz = np.sin(2 * np.pi * xv) * np.cos(2 * np.pi * yv)

# Create a new figure
fig = plt.figure(figsize=(7.0, 5.0))

# Plot the contour
plt.contourf(xv, yv, Bz, cmap=plt.cm.viridis)
plt.title("Contour of Bz")
plt.xlabel("y")
plt.ylabel("x")
plt.colorbar()

# Show the plot
plt.show()
```