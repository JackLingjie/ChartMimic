```python
import matplotlib.pyplot as plt  
import numpy as np  
import squarify

# Sample data
sizes = [15, 30, 45, 10]
labels = ["A: 15", "B: 30", "C: 45", "D: 10"]

# Create a new figure
fig = plt.figure(figsize=(6.0, 4.0))

# Plot the treemap
squarify.plot(sizes=sizes, label=labels, alpha=0.7)
plt.axis('off')
plt.title("Most Mentioned Picks")

# Show the plot
plt.show()
```