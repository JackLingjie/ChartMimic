```python
import numpy as np  
import matplotlib.pyplot as plt  
from matplotlib import cm  

# Define the size and create a meshgrid  
size = 1000  
x = np.arange(0.0, np.pi, np.pi/size)  
y = np.arange(0.0, np.pi, np.pi/size)  
X, Y = np.meshgrid(x, y)  

# Calculate the result  
result = np.sin(X) * np.sin(Y)  

# Create a new figure  
fig, ax = plt.subplots(figsize=(7.0, 7.0))  

# Plot the contour  
cs = ax.contourf(X, Y, result, cmap=cm.gist_rainbow)  

# Add a colorbar  
cbar = fig.colorbar(cs)  

# Show the plot  
plt.show()
```