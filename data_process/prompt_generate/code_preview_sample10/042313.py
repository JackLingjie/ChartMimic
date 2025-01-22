```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data  
days = np.array([1, 2, 3, 4, 5])  
sleeping = np.array([7, 8, 9, 12, 6])  
eating = np.array([2, 3, 4, 3, 2])  
working = np.array([7, 8, 7, 2, 2])  
playing = np.array([8, 5, 7, 8, 13])  

# Create a new figure  
plt.figure(figsize=(6.0, 4.0))  

# Plot the stackplot  
plt.stackplot(days, sleeping, eating, working, playing, colors=['r', 'm', 'k', 'c'], labels=['Sleeping', 'Eating', 'Working', 'Playing'])  

# Set labels and title  
plt.xlabel('Days')  
plt.ylabel('Hours')  
plt.title('Daily Activities')  

# Add a legend  
plt.legend(loc='upper left')  

# Show the plot  
plt.show()
```