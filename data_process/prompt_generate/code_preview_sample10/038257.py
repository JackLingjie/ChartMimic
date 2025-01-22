```python
import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
y_err = 0.2

# Create a new figure
plt.figure(figsize=(6.0, 4.0))

# Plot the data with error fill
plt.plot(x, y, label='sin(x)')
plt.fill_between(x, y - y_err, y + y_err, alpha=0.2, label='Error')

# Set labels
plt.xlabel('X')
plt.ylabel('Y')

# Add a legend
plt.legend()

# Show the plot
plt.show()
```