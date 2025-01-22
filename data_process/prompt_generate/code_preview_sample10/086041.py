```python
import numpy as np  
import matplotlib.pyplot as plt  

# Generate data grid  
x = np.linspace(-10, 10, 50)  
y = np.linspace(-10, 10, 50)  
X, Y = np.meshgrid(x, y)  

# Generate data points  
Z = np.sin(X) + np.cos(Y)  

# Display contour plot  
plt.figure(figsize=(6.0, 4.0))  
plt.contour(X, Y, Z, 20, cmap='RdGy')  
plt.colorbar()  

plt.show()
```