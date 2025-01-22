```python
import numpy as np  
import matplotlib.pyplot as plt  

# Parameters
NFFT = 16
DEL = 0

# Generate data
n = np.arange(NFFT)
x = np.zeros(NFFT)
x[DEL] = NFFT

# Create a new figure
fig = plt.figure(figsize=(6, 3))
ax = fig.add_subplot(111)

# Plot the data
markerline, stemlines, baseline = ax.stem(n, x)
plt.setp(markerline, 'markerfacecolor', 'k', 'markersize', 8, 'marker', 's')
plt.setp(stemlines, 'color', 'b', 'linewidth', 1)
plt.setp(baseline, 'linewidth', 0)

# Set labels
ax.set_xlabel('n →')
ax.set_ylabel('x[n] →')
ax.set_xlim([-1, NFFT])
ax.set_ylim([-1, NFFT + 1])

# Show the plot
plt.show()
```