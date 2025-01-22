```python
import matplotlib.pyplot as plt  
import numpy as np  
import matplotlib.patches as patches  

# Sample data for bounding boxes
result = [[(0.1, 0.2, 0.3, 0.4), (0.5, 0.6, 0.2, 0.3)]]

# Create a new figure
fig, ax = plt.subplots(figsize=(6.0, 4.0))

# Display a blank image
ax.imshow(np.zeros((10, 10)), cmap="gray")

# Draw rectangles
for j in range(0, len(result[0])):
    bx, by, bw, bh = result[0][j]
    rect = patches.Rectangle((bx*11.0 - 0.5, by*11.0 - 0.5), bw*11.0, bh*11.0, linewidth=1, edgecolor="r", facecolor="none")
    ax.add_patch(rect)

plt.show()
```