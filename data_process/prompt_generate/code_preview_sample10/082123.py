```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
data = np.array([[10, 11, 13, 15],
                 [13, 15, 18, 21],
                 [16, 19, 22, 26],
                 [20, 23, 27, 31]])
xlabels = np.array([12, 13, 14, 15])
ylabels = np.array([2, 3, 4, 5])

# Create a new figure
fig, ax = plt.subplots(figsize=(6.0, 4.0))
im = ax.imshow(data, cmap='GnBu')
ax.set_xticks(np.arange(len(xlabels)))
ax.set_xticklabels(xlabels)
ax.xaxis.tick_top()
ax.set_xlabel('Resolution (divided by 10^3)')
ax.xaxis.set_label_position('top')
ax.set_yticks(np.arange(len(ylabels)))
ax.set_yticklabels(ylabels)
ax.set_ylim(3.5, -0.5)
ax.set_ylabel('Iterations')
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Time (sec)', rotation=-90, va='bottom')

for x_idx in range(len(xlabels)):
    for y_idx in range(len(ylabels)):
        ax.text(x_idx, y_idx, data[x_idx, y_idx],
                ha="center", va="center", color="k")

fig.tight_layout()
plt.show()
```