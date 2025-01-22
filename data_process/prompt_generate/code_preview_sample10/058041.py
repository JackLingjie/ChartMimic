```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data for class distribution
labels = ['Class A', 'Class B', 'Class C']
sizes = [30, 45, 25]

# Create a new figure
fig, ax = plt.subplots(figsize=(6.0, 6.0))

# Plot a pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.set_title('Class Distribution')

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Show the plot
plt.show()
```