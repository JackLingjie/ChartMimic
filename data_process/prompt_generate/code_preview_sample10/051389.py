```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
base_bars = [1.0, 1.0, 1.0, 1.0, 1.0]
flex_bars = [0.9, 1.1, 0.95, 1.05, 1.0]
x = np.arange(len(base_bars))

# Create a new figure
plt.figure(figsize=(6.0, 4.0))

# Plot the bars
plt.bar(x, base_bars, width=0.4, label="numpy", color="g")
plt.bar(x + 0.4, flex_bars, width=0.4, label="flextensor", color="r")

# Add a legend
plt.legend()

# Show the plot
plt.show()
```