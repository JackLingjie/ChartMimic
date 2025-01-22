```python
import matplotlib.pyplot as plt  
from matplotlib.patches import Rectangle  
import numpy as np  

# Sample data for obstacles and goals
obstacles = np.array([[1, 2], [3, 4], [5, 6]])
goals = np.array([[2, 3], [4, 5]])

# Create a new figure
fig = plt.figure(figsize=(6.0, 6.0))  
ax = fig.add_subplot(111, aspect='equal')  

# Set limits
plt.xlim(-0.5, 6.5)
plt.ylim(-0.5, 6.5)

# Plot obstacles
for o in obstacles:
    ax.add_patch(Rectangle((o[0] - 0.5, o[1] - 0.5), 1, 1, facecolor='red', edgecolor='black'))

# Plot goals
for g in goals:
    ax.add_patch(Rectangle((g[0] - 0.4, g[1] - 0.4), 0.8, 0.8, facecolor='green', edgecolor='black'))

# Show the plot
plt.show()
```