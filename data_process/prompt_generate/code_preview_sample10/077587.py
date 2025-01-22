```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data  
data = np.array([-0.38763, 0.80928, 1.5736, -0.19156, -1.2762, 0.012471, 2.7392, -0.14373, 1.5309, -0.71012, 2.6883,  
                 -0.97024, -0.18379, 0.39052, 0.89383, -0.28856, -0.82227, -1.2461, 2.8595, 0.50082])

# Create a new figure  
fig = plt.figure(figsize=(6, 6))  
ax = fig.add_subplot(111)  

# Plot the data as a histogram  
ax.hist(data, bins=10, color='#365994', alpha=0.7)  

# Set labels  
ax.set_xlabel('Value')  
ax.set_ylabel('Frequency')  

# Show the plot  
plt.show()
```