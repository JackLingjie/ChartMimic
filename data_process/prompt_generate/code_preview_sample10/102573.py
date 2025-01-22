```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
X = np.array([0, 1, 2, 3])
Y = np.array([0, 1, 2, 3])
U = np.array([1, -1, -1, 0.5])
V = np.array([-0.5, -1.5, -0.5, -2])
R = np.sqrt(U**2 + V**2)

# Create a new figure
plt.figure(figsize=(6.0, 6.0))  

# Quiver plot
plt.quiver(X, Y, U / R * R.max(), V / R * R.max(), alpha=0.5)
plt.quiver(X,Y,U,V,color='blue',edgecolor='k',facecolor='None',linewidth=0.5)

r=3.0 # Plot range limit
plt.xlim(-r,r)
plt.xticks(())
plt.ylim(-r,r)
plt.yticks(())

# Display the plot
plt.show()
```