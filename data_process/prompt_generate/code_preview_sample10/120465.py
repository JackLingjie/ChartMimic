```python
import matplotlib.pyplot as plt  
import matplotlib.patches as mpatches  
import numpy as np  

# Create the figure and axes with specified size
fig, ax = plt.subplots(figsize=(6.0, 6.0), subplot_kw={'projection': 'polar'})

# Hide the spines and ticks
ax.spines['polar'].set_visible(False)  
ax.xaxis.set_visible(False)  
ax.yaxis.set_visible(False)  

# Define variables for plotting
p0 = (0, 0)
a0 = 0
a1 = np.pi / 8
a2 = 2 * a1
a3 = a2 + np.pi / 2 + .15
a4 = np.pi + .5

# Plot rays using FancyArrowPatch
list_patches1 = []
ray_angles = [a0, a1, a2, a3, a4]
for angle in ray_angles:
    ray_patch = mpatches.FancyArrowPatch(p0, (angle, 1), arrowstyle='->', mutation_scale=12)
    list_patches1.append(ray_patch)

plt.scatter(p0[0], p0[1], s=6, color='k')
for patch in list_patches1:
    ax.add_patch(patch)

# Draw arcs to represent angles between rays 
angles_and_radii_pairs = [
    (np.linspace(a0, a4, 30), .200),
    (np.linspace(a0,a2 ,30), .215),
    (np.linspace(a3,a4 ,30), .215),
]

for angles,radius in angles_and_radii_pairs:
     ax.plot(angles,radius*np.ones(len(angles)),'k',linewidth=1)

plt.show()
```