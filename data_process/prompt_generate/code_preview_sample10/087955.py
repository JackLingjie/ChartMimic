```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
categories = ['RMSE', 'MAPE', 'R^2']
values = [16.716, 3.0125, 0.9915]

# Create a new figure
fig = plt.figure(figsize=(6.0, 6.0))

# Create a radar chart
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

ax = plt.subplot(111, polar=True)
ax.fill(angles, values, color='teal', alpha=0.25)
ax.plot(angles, values, color='teal', linewidth=2)

# Add labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Show the plot
plt.show()
```