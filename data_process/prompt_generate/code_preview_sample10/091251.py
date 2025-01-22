```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data  
x = np.array([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])  
y = np.array([0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1])  

# Create a new figure  
fig = plt.figure(figsize=(6.0, 4.0))  

# Plot the data  
plt.plot(x, y, 'bo', markersize=3)  

# Set labels  
plt.xlabel('X')  
plt.ylabel('Y')  

# Show the plot  
plt.show()
```