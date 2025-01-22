```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
data = np.array([3, 5, 7])

# Create a new figure
plt.figure(figsize=(7.0, 5.0))

# Plot the data
plt.bar([0, 1, 2], data, color=['C0', 'C1', 'C2'], alpha=0.7)

# Set labels
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Sample Bar Plot')

# Show the plot
plt.show()
```