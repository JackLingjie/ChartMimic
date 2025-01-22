```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
NUM1 = np.array([1, 10, 100, 1000, 10000])
TIME1 = np.array([0.1, 0.2, 0.3, 0.4, 0.5])

# Create a new figure
plt.figure(figsize=(6.0, 4.0))

# Plot the data
plt.plot(NUM1, TIME1, 'bo-', label='Parallel')

# Set labels and title
plt.title('Sieve of Eratosthenes')
plt.xlabel("n")
plt.ylabel('Time (s)')

# Add a legend
plt.legend()

# Set x-axis to logarithmic scale
plt.xscale('log')

# Show the plot
plt.show()
```