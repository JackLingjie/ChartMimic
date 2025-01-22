```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data  
x = np.array([1])  
y = np.array([0.8])  
Ty = np.array([0.9])  
yw = np.array([0.85])  
Twy = np.array([0.88])  

# Create a new figure  
plt.figure(figsize=(6.0, 4.0))  

# Plot the data  
plt.scatter(x, y, color='g', label='Test Set')  
plt.scatter(x, Ty, color='b', label='Train Set')  
plt.scatter(x, yw, color='r', label='Test Set W')  
plt.scatter(x, Twy, color='salmon', label='Train Set W')  

# Add a legend  
plt.legend(loc='lower left')  

# Show the plot  
plt.show()
```