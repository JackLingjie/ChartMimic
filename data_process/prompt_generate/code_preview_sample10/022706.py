```python
import matplotlib.pyplot as plt  
import numpy as np  
from mpl_toolkits.mplot3d import Axes3D  

# Sample data  
azimuth = np.radians(np.linspace(start=0, stop=360, num=361, endpoint=True))  
colatitude = np.radians(np.linspace(start=0, stop=180, num=180, endpoint=True))  

# Create a new figure  
fig = plt.figure(figsize=(7.0, 7.0))  
ax = fig.add_subplot(111, projection='3d')  

# Sample 3D surface plot  
AZI, COL = np.meshgrid(azimuth, colatitude)  
X = np.sin(COL) * np.cos(AZI)  
Y = np.sin(COL) * np.sin(AZI)  
Z = np.cos(COL)  
ax.plot_surface(X, Y, Z, cmap='viridis')  

# Set labels  
ax.set_xlabel('X')  
ax.set_ylabel('Y')  
ax.set_zlabel('Z')  

# Show the plot  
plt.show()
```