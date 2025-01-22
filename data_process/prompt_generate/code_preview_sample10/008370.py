```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
x = np.linspace(-np.pi, np.pi, 100)
y1 = np.cos(x) - 1
y2 = np.cos(x)

# Create a new figure
fig = plt.figure(figsize=(6.0, 4.0))

# Plot the area between the curves
plt.fill_between(x, y1, y2, color='lightblue', alpha=0.5)

# Set labels
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()
```