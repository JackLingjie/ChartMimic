```python
import matplotlib.pyplot as plt  
import numpy as np  
from matplotlib.patches import Circle  
from matplotlib.offsetbox import AnnotationBbox, OffsetImage  

fig, ax = plt.subplots(figsize=(7.0, 7.0))

# Define a position to annotate
xy = (0.5, 0.7)
ax.plot(xy[0], xy[1], ".r")

# Annotate the position with an image (a generated array of pixels)
arr = np.arange(100).reshape((10, 10))
im = OffsetImage(arr, zoom=2)
im.image.axes = ax

ab = AnnotationBbox(im, xy,
                    xybox=(-50., 50.),
                    xycoords='data',
                    boxcoords="offset points",
                    pad=0.3,
                    arrowprops=dict(arrowstyle="->"))

ax.add_artist(ab)

# Fix the display limits to see everything
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()
```