```python
import numpy as np  
import matplotlib.pyplot as plt  
from matplotlib.patches import PathPatch  
from matplotlib.path import Path  

# Define vertices and codes for the path
vertices = np.array([(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)], float)
codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]

# Create a path and a patch
path = Path(vertices, codes)
pathpatch = PathPatch(path, facecolor='None', edgecolor='green')

# Create a new figure with specified size
fig = plt.figure(figsize=(6.0, 4.0))
ax = fig.add_subplot(111)

# Add the path patch to the axes
ax.add_patch(pathpatch)
ax.set_title('A compound path')

# Set limits and autoscale view based on vertices data 
ax.dataLim.update_from_data_xy(vertices)
ax.autoscale_view()

# Display the plot
plt.show()
```