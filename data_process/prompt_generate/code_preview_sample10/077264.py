```python
import matplotlib.pyplot as plt  
import numpy as np  

# Define x and y values  
x = np.arange(0, 10, 0.1)  
y = np.arange(10, 20, 0.1)  

# Create plot of values  
plt.figure(figsize=(7.0, 5.0))  
plt.plot(x, y)  

# Fill in area between the two lines  
plt.fill_betweenx(y, 2, 4, color='red', alpha=0.5)  

# Create a title for the graph  
plt.title("Figure 4")  

# Show the plot  
plt.show()
```