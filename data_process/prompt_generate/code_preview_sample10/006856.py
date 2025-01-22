```python
import numpy as np  
import matplotlib.pyplot as plt  

# Create a new figure with specified size
fig = plt.figure(figsize=(6.0, 6.0))  
ax = fig.add_subplot()  

# Generate data
u = np.linspace(-1, 1, 100)  
x, y = np.meshgrid(u, u)  
z = x ** 2 + y ** 2  

# Plot contour
ax.contour(x, y, z)  

# Show the plot
plt.show()
```