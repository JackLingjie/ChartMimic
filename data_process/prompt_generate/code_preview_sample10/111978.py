```python
import matplotlib.pyplot as plt  
from mpl_toolkits.axes_grid1 import make_axes_locatable  

# Create a new figure with specified size
fig = plt.figure(figsize=(6.0, 3.0))  

ax = fig.add_subplot(111)
im = ax.imshow([[1, 2], [3, 4]])

# Use axes divider to add an axis for the colorbar
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="7%", pad="2%")
cb = plt.colorbar(im, cax=cax)

# Show the plot
plt.show()
```