```python
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  
import numpy as np  

# Sample data
grc_pos = np.array([
    [0.1, 0.2, 0.3],
    [0.2, 0.3, 0.4],
    [0.3, 0.4, 0.5],
    [0.4, 0.5, 0.6]
])

glom_pos = np.array([
    [0.5, 0.6, 0.7],
    [0.6, 0.7, 0.8],
    [0.7, 0.8, 0.9],
    [0.8, 0.9, 1.0]
])

# Create a new figure
fig = plt.figure(figsize=(7.0, 7.0))  
ax = fig.add_subplot(111, projection='3d')  

# Plot the positions
ax.plot(grc_pos[:, 0], grc_pos[:, 1], grc_pos[:, 2], c='b', marker='o', linestyle='', label='GRC Positions')  
ax.plot(glom_pos[:, 0], glom_pos[:, 1], glom_pos[:, 2], c='r', marker='o', linestyle='', label='Glom Positions')  

# Set labels
ax.set_xlabel('X')  
ax.set_ylabel('Y')  
ax.set_zlabel('Z')  

# Add a legend
ax.legend()  

# Show the plot
plt.show()
```