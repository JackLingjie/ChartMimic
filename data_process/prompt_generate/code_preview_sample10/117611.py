```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
x = np.linspace(-4.5, 3.5, 1000)
density = np.exp(-0.5 * (x - 1)**2) / (np.sqrt(2 * np.pi))

# Create a new figure
plt.figure(figsize=(6.0, 4.0))

# Plot the density
plt.plot(x, density, color='blue', alpha=0.5, lw=3)

# Show the plot
plt.show()
```