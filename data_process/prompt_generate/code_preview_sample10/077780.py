```python
import numpy as np  
import matplotlib.pyplot as plt  

# Sample data  
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])  

# Create a new figure  
plt.figure(figsize=(6.0, 4.0))  

# Plot the histogram  
plt.hist(a, bins=[0, 20, 40, 60, 80, 100])  
plt.title("Histogram")  
plt.xlabel("Value")  
plt.ylabel("Frequency")  

# Show the plot  
plt.show()
```