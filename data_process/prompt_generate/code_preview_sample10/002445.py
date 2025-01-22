```python
import matplotlib.pyplot as plt  
from matplotlib import patches  

# Create a new figure with specified size
fig = plt.figure(figsize=(7.0, 5.0))  
ax = fig.add_subplot(111)  

# Set x-axis limits
plt.xlim(0, 10)  

# Sample data
tans = [(1, 0, 4), (0, 4, 3), (1, 7, 3)]
tpred = [(1, 0, 2), (0, 2, 2), (1, 4, 1), (0, 5, 2), (1, 7, 1), (0, 8, 2)]

# Plot rectangles for tans
for a in tans:  
    col = (.8, .2, .2) if a[0] == 1 else (.2, .8, .2)  
    ax.add_patch(patches.Rectangle((a[1], 0), a[2], 0.5, color=col))  

# Plot rectangles for tpred
for a in tpred:  
    col = (.8, .2, .2) if a[0] == 1 else (.2, .8, .2)  
    ax.add_patch(patches.Rectangle((a[1], 0.5), a[2], 0.5, color=col))  

# Show the plot
plt.show()
```