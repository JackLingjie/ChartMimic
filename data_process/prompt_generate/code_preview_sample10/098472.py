```python
import numpy as np
import matplotlib.pyplot as plt

# Sample data
angles = np.linspace(0, 2 * np.pi, 100)
radii = np.abs(np.sin(angles))

# Create a new figure with polar projection
fig, ax = plt.subplots(figsize=(6.0, 6.0), subplot_kw={'polar': True})

# Plot the data
ax.plot(angles, radii)

# Set labels and title
ax.set_title('Sample Polar Plot', va='bottom')

# Show the plot
plt.show()
```