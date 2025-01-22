```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 3, 2, 5, 4]

# Calculate angles for radar chart
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

# Create a new figure
fig = plt.figure(figsize=(6.0, 6.0))
ax = plt.subplot(111, polar=True)

# Plot data
ax.plot(angles, values, linewidth=2, linestyle='solid', label='Sample Data')
ax.fill(angles, values, 'b', alpha=0.1)

# Set category labels
plt.xticks(angles[:-1], categories)

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Show the plot
plt.show()
```