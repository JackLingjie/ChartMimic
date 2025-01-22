```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = [1, 2, 3, 4, 5]
y = [3, 2, 7, 6, 8]
z = [7, 9, 0, 5, 4]
data = [x, y, z]

# Create a new figure
plt.figure(figsize=(6.0, 4.0))

# Plot the data
plt.boxplot(data, showmeans=True)

# Set title
plt.title('Box plot')

# Show the plot
plt.show()
```