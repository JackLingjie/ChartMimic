```python
import numpy as np
import matplotlib.pyplot as plt

# Sample data
X = np.array([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
Y = np.array([0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1])

# Create a new figure
plt.figure(figsize=(7.0, 5.0))

# Plot the data
plt.scatter(X, Y, color='blue', label='Data Points')

# Set labels
plt.xlabel('X')
plt.ylabel('Y')

# Add a legend
plt.legend()

# Show the plot
plt.show()
```