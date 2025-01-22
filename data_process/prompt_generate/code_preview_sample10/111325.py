```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
amounts = np.array([100, 200, 300, 400, 500])
units = np.array([1, 2, 3, 4, 5])

# Create a new figure
plt.figure(figsize=(6.0, 4.0))  

# Scatter plot
plt.scatter(amounts, units)
plt.xlabel("Amount ($)")
plt.ylabel("Units")
plt.title("Units vs Amount")

# Show the plot
plt.show()
```