```python
import matplotlib.pyplot as plt
import numpy as np

# Sample correlation matrix for demonstration
correlation = np.array([
    [1.0, 0.8, 0.6],
    [0.8, 1.0, 0.5],
    [0.6, 0.5, 1.0]
])

# Create a new figure with specified size
fig = plt.figure(figsize=(6.4, 4.8))

# Plotting the heatmap of correlation matrix
plt.imshow(correlation, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.title("Correlation Matrix")
plt.show()
```