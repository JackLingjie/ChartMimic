```python
import matplotlib.pyplot as plt  
import numpy as np  
from mpl_toolkits.mplot3d import Axes3D  

# Data  
fx = [0.673574075, 0.727952994, 0.6746285]  
fy = [0.331657721, 0.447817839, 0.37733386]  
fz = [18.13629648, 8.620699842, 9.807536512]  

# Error data  
xerror = [0.041504064, 0.02402152, 0.059383144]  
yerror = [0.015649804, 0.12643117, 0.068676131]  
zerror = [3.677693713, 1.345712547, 0.724095592]  

# Create a new figure  
fig = plt.figure(figsize=(7.0, 7.0))  
ax = fig.add_subplot(111, projection='3d')  

# Plot points  
ax.plot(fx, fy, fz, linestyle="None", marker="o")  

# Plot error bars  
for i in range(len(fx)):  
    ax.plot([fx[i] + xerror[i], fx[i] - xerror[i]], [fy[i], fy[i]], [fz[i], fz[i]], marker="_")  
    ax.plot([fx[i], fx[i]], [fy[i] + yerror[i], fy[i] - yerror[i]], [fz[i], fz[i]], marker="_")  

# Configure axes  
ax.set_xlim3d(0.55, 0.8)  
ax.set_ylim3d(0.2, 0.5)  
ax.set_zlim3d(8, 19)  

# Show the plot  
plt.show()
```