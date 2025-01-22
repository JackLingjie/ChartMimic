```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
omega_N = np.array([78.54, 63.66, 41.36, 51.32, 82.68, 92.83, 99.95, 110.57, 123.17, 53.93])
omega_F = np.array([81.68, 65.45, 43.98, 52.36, 83.78, 94.25, 108.01, 116.89, 132.59, 55.45])
d_omega_F = np.array([1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05])

# Create a new figure
plt.figure(figsize=(7.0, 5.0))

# Plot the data with error bars
plt.errorbar(omega_N, omega_F, yerr=d_omega_F, fmt='o', label='Data')

# Set labels
plt.xlabel('ω_N / (1/s)')
plt.ylabel('ω_F / (1/s)')

# Add a legend
plt.legend()

# Show the plot
plt.show()
```