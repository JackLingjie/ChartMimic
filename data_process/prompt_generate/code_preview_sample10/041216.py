```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
rad = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
data1 = np.array([1.0, 0.8, 0.6, 0.4, 0.2])
err1 = np.array([0.05, 0.04, 0.03, 0.02, 0.01])

# Create a new figure
plt.figure(figsize=(6.0, 4.0))

# Plot with error bars
plt.errorbar(rad, data1, yerr=err1, ecolor='r', capsize=1.0, ls='--', label="g(r)")

# Add a legend
plt.legend()

# Show the plot
plt.show()
```