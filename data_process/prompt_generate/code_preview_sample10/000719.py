```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
x = np.array([0.2, 0.5, 1.5])
y = np.array([0.2, 0.5, 1.5])
colors = ['blue', 'green', 'red']

# Create a new figure
fig = plt.figure(figsize=(6.0, 4.0))

# Plot the points
plt.scatter(x, y, c=colors, s=100)

# Set labels
plt.xlabel('X')
plt.ylabel('Y')

# Show the plot
plt.show()
```