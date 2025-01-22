```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure
fig = plt.figure(figsize=(7.0, 5.0))
ax = plt.axes()

# Add a sample rectangle
x1, y1, x2, y2 = 1, 1, 3, 4
ax.add_patch(patches.Rectangle((x1, y1), x2 - x1, y2 - y1, fill=False, edgecolor='black'))

# Set grid
plt.grid(color='b', linewidth=0.3, linestyle='--')

# Show the plot
plt.show()
```