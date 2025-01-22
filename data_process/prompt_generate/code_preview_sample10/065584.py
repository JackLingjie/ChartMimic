```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
categories = ['cil-acc', 'til-acc', 'iil-acc']
values = [84.0, 93.0, 84.0]

# Number of variables
N = len(categories)

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

# The values must be repeated to close the circle
values += values[:1]

# Initialise the spider plot
fig, ax = plt.subplots(figsize=(6.0, 6.0), subplot_kw=dict(polar=True))

# Draw one axe per variable + add labels
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([70, 80, 90], ["70", "80", "90"], color="grey", size=7)
plt.ylim(60, 100)

# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid', label='Example Group')

# Add legend
plt.legend()

# Show the plot
plt.show()
```