```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data  
blood_sugar = [113, 85, 90, 150, 149, 88, 93, 115, 80, 77, 82, 129]

# Create a new figure  
plt.figure(figsize=(7.0, 5.0))  

# Plot the histogram  
plt.hist(blood_sugar, bins=5, rwidth=0.90)  

# Show the plot  
plt.show()
```