```python
import matplotlib.pyplot as plt  
import numpy as np  

# Define parameters
theta = np.array([[-4], [0.5], [1]])

# Create a new figure
fig, ax = plt.subplots(figsize=(7.0, 7.0))

# Generate grid data
xs = np.linspace(-4, 8, 200)
ys = np.linspace(-4, 8, 200)
xsgrid, ysgrid = np.meshgrid(xs, ys)
plane = np.zeros_like(xsgrid)

# Calculate plane values
for i in range(xsgrid.shape[0]):
    for j in range(xsgrid.shape[1]):
        plane[i, j] = np.array([1, xsgrid[i, j], ysgrid[i, j]]).dot(theta)

# Plot contour
cs = ax.contour(xsgrid, ysgrid, plane, levels=[0])
cs.clabel(inline=1)

# Add annotations
ax.annotate('here y_hat(x) > 0', xy=(4, 4), fontsize=10)
ax.annotate('here y_hat(x) < 0', xy=(0, 0), fontsize=10)

# Show the plot
plt.show()
```