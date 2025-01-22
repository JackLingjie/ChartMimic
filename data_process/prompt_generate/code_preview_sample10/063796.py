```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

# Create a new figure
fig = plt.figure(figsize=(7.0, 7.0))
ax = fig.add_subplot(111, projection='3d')

# Get test data
X, Y, Z = axes3d.get_test_data(0.05)

# Plot surface
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3, cmap=cm.coolwarm)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
```