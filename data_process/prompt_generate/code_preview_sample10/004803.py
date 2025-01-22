```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
categories = ['Win Pct', 'AWP', 'SOS', 'PPG', 'MOV', 'Streak']
values = [0.8, 0.9, 0.7, 0.6, 0.5, 0.4]

# Create a new figure
fig = plt.figure(figsize=(6.0, 6.0))

# Number of variables
N = len(categories)

# Create a radar chart
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

ax = plt.subplot(111, polar=True)
ax.fill(angles, values, color='green', alpha=0.25)
ax.plot(angles, values, color='green', linewidth=2)

# Set the category labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Show the plot
plt.show()
```