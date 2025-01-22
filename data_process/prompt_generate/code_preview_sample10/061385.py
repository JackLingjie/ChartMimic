```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
ages = np.array([1, 2, 3, 4, 5, 6, 7])
purchases = np.array([8370, 15200, 1422, 1057, 7969, 15227, 19215])

# Create a new figure
fig = plt.figure(figsize=(7.0, 5.0))

# Plot the data
plt.bar(ages, purchases, color='blue', label='Purchases')

# Set labels
plt.xlabel('Age Group')
plt.ylabel('Purchase Amount')

# Add a legend
plt.legend()

# Show the plot
plt.show()
```