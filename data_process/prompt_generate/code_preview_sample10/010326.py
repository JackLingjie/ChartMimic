```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
family_ages = [21, 22, 3, 44, 45, 18, 91, 102, 65, 54, 32, 31, 6, 12, 45, 78, 43, 27, 99, 32, 87, 90, 53, 28, 22, 67, 60]

# Create a new figure
plt.figure(figsize=(7.0, 5.0))

# Plot the histogram
plt.hist(family_ages, bins=10)

# Set labels
plt.xlabel("Ages")
plt.ylabel("Count")

# Show the plot
plt.show()
```