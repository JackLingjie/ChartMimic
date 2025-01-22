```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data  
ages = [10, 56, 45, 78, 25, 36, 95, 84, 19, 65, 29, 45, 78, 10, 22, 55, 99, 46, 50, 78, 83, 93, 97, 102, 103, 8, 13, 58, 65, 75, 12, 59, 30, 56, 90, 70, 40, 59, 29, 34, 51, 53, 82, 88]  
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]  

# Create a new figure  
plt.figure(figsize=(6.0, 4.0))  

# Plot the histogram  
plt.hist(ages, bins=bins, histtype='bar', rwidth=0.8)  

# Set labels and title  
plt.xlabel('Age')  
plt.ylabel('Frequency')  
plt.title('Age Distribution')  

# Show the plot  
plt.show()
```