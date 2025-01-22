```python
import matplotlib.pyplot as plt  
import numpy as np  

# Data for the pie chart
fruit = ['apple', 'orange', 'mango', 'guava']
quantity = [67, 34, 100, 29]

# Create a new figure with specified size
plt.figure(figsize=(6.0, 6.0))

# Plot the outer pie chart
plt.pie(quantity, labels=fruit, radius=1)

# Plot the inner circle to create a doughnut chart
plt.pie([1], colors=['w'], radius=0.5)

# Show the plot
plt.show()
```