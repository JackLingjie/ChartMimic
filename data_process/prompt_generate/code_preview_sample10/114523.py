```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data for vectors a and b
a = np.array([0.6, 0.3, 0.9])
b = np.array([0.4, 0.8, 0.2])

# Create a new figure
fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_subplot(111, projection='3d')

# Plot the basis vectors and the bivector (area spanned by vectors a and b)
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label='Vector A')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='b', label='Vector B')

# Set view angle
ax.view_init(azim=20,elev=20)

# Set axis limits
ax.set_xlim((0, 1))
ax.set_ylim((0, 1))
ax.set_zlim((-1 ,1))

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.tight_layout()
plt.show()
```