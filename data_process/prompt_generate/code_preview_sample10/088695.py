```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data  
spec11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  
spec52 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  
spec100 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  

# Create a new figure  
fig = plt.figure(figsize=(6.0, 4.0))  
ax = fig.add_subplot(111)  

# Plot the data  
ax.boxplot([spec11, spec52, spec100], labels=['11', '52', '100'])  

# Set labels  
plt.xlabel('Number of Species', fontsize=14)  
plt.ylabel('Bandwidth in MiB/s', fontsize=14)  

# Set title  
fig.suptitle("16 Procs", fontsize=20)  

# Show the plot  
plt.show()
```