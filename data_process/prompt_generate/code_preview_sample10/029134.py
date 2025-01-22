```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data for radar chart
labels = np.array(['Agility', 'Speed', 'Strength'])
values = np.array([5, 3, 10])
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is a circle, so we need to "complete the loop" and append the start value to the end.
values = np.concatenate((values, [values[0]]))
angles += angles[:1]

# Create a new figure
fig, ax = plt.subplots(figsize=(6.0, 6.0), subplot_kw=dict(polar=True))

# Draw one line per variable and fill the area
ax.fill(angles, values, color='orange', alpha=0.25)
ax.plot(angles, values, color='orange', linewidth=2)

# Add labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# Show the plot
plt.show()
```