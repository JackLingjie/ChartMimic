```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a new figure
plt.figure(figsize=(6.0, 4.0))

# Plot the data
plt.plot(x, y, label='Sine Wave')

# Set labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave Plot')

# Add a legend
plt.legend()

# Show the plot
plt.show()
```