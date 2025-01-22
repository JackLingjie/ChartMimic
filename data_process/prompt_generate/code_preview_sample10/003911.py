```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
coords = np.array([
    (0.0, 0.0),
    (-0.5, np.sqrt(3) / 2),
    (0.5, np.sqrt(3) / 2),
    (1.0, 0.0),
    (0.5, -np.sqrt(3) / 2),
    (-0.5, -np.sqrt(3) / 2)
])

# Set the figure size
fig, ax = plt.subplots(figsize=(6.0, 6.0))

# Plot the points
ax.scatter(coords[:, 0], coords[:, 1], s=30, alpha=0.7, c="darkgreen")

# Set labels
ax.set_xlabel("µm")
ax.set_ylabel("µm")
ax.axis("equal")

# Show the plot
plt.show()
```