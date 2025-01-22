```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.array([
    [100, 12.13, 367.19, 213.85],
    [1000, 39.48, 381.16, 214.17],
    [5000, 158.51, 381.67, 215.11],
    [10000, 313.93, 373.39, 222.55],
    [20000, 614.61, 373.57, 222.99],
    [35000, 1065.35, 377.65, 220.66],
    [50000, 1530.08, 376.60, 225.07]
])

xs = data[:, 0]
ys = data[:, 1]

# Create a new figure
plt.figure(figsize=(7.0, 5.0))

# Plot the data
plt.plot(xs, ys, ls='--', marker='o', label="svtyper")

# Set labels
plt.xlabel("Number of variants")
plt.ylabel("Time (seconds)")

# Add a legend
plt.legend()

# Show the plot
plt.show()
```