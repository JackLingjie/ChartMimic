```python
import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.linspace(0, 1, 500)
y = np.sin(10 * 2 * np.pi * x) * np.exp(-5 * x)

# Create a new figure
plt.figure(figsize=(6.0, 4.0))

# Plot the data
plt.fill(x, y, 'r')

# Add grid
plt.grid(True)

# Show the plot
plt.show()
```