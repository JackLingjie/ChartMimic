```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
x_vals = np.array([100, 200, 300, 400, 500])
y_vals = np.array([0.1, 0.2, 0.15, 0.3, 0.25])
x_err_vals = np.array([10, 20, 15, 25, 20])
y_err_vals = np.array([0.01, 0.02, 0.015, 0.03, 0.025])

# Create a new figure
plt.figure(figsize=(6.0, 4.0))

# Plot with error bars
plt.errorbar(x_vals, y_vals, xerr=x_err_vals, yerr=y_err_vals, fmt='o', label='Data with error')

# Set labels
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase Difference (radians)')

# Set x-axis to log scale
plt.xscale('log')

# Add a legend
plt.legend()

# Show the plot
plt.show()
```