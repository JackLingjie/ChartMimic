```python
import matplotlib.pyplot as plt  
import numpy as np  

# Define the sphere function
def sphere(x):
    return np.sum(x**2, axis=0)

# Create a grid of points
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = sphere(np.array([X, Y]))

# Create a new figure
fig = plt.figure(figsize=(7.0, 5.0))

# Plot the contours
plt.contour(X, Y, Z, levels=20, cmap='viridis')

# Set labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sphere Function Contour')

# Show the plot
plt.show()
```