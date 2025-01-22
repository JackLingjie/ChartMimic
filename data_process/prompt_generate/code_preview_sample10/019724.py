```python
import numpy as np  
import matplotlib.pyplot as plt  

# Sample data  
women_pop = np.array([5., 30., 45., 22.])  
men_pop = np.array([5., 25., 50., 20.])  
X = np.arange(4)  

# Create a new figure  
plt.figure(figsize=(6.0, 4.0))  

# Plot the data  
plt.barh(X, women_pop, color='r', label='Women')  
plt.barh(X, -men_pop, color='b', label='Men')  

# Add a legend  
plt.legend()  

# Show the plot  
plt.show()
```