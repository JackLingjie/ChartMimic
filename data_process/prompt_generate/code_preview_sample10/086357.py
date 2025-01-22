```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
area_values = [12, 17, 14, 15, 20, 28, 30, 28, 10]

# Create a new figure
fig = plt.figure(figsize=(6.0, 4.0))
ax = fig.add_subplot(111)

# Plot the area
ax.fill_between(np.arange(9), area_values, color='skyblue', alpha=0.5)
ax.plot(np.arange(9), area_values, color='black', alpha=0.6, linewidth=2)

# Show the plot
plt.show()
```