```python
import matplotlib.pyplot as plt  
import numpy as np  

# Create a grid of points
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)

# Define a covariance matrix for a Gaussian distribution
covariance_matrix = np.array([[4.0, 0.0], [0.0, 1.0]])
loc = np.array([0.0, 0.0])

# Calculate the Gaussian distribution
Z = np.exp(-0.5 * ((X - loc[0])**2 / covariance_matrix[0, 0] + (Y - loc[1])**2 / covariance_matrix[1, 1]))

# Plot the contour
plt.figure(figsize=(6.0, 6.0))
CS = plt.contour(X, Y, Z)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Control scaled noise')
plt.axis("equal")
plt.grid(True)
plt.show()
```