```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
X = np.array([[1, 1], [2, 3], [1, 3], [7, 8], [6, 9], [6, 7]])

# Create a new figure
plt.figure(figsize=(6.0, 4.0))

# Plot the data points
plt.scatter(X[:, 0], X[:, 1], color='blue', label='Data Points')

# Set labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend
plt.legend()

# Show the plot
plt.show()
```