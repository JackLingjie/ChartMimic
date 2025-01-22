```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data  
labels = ['A', 'B', 'C', 'D']  
sizes = [15, 30, 45, 10]  

# Create a new figure  
fig = plt.figure(figsize=(6.0, 6.0))  

# Plot a pie chart  
plt.pie(sizes, labels=labels)  
plt.title("Market Distribution")  

# Show the plot  
plt.show()
```