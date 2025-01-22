```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
labels = ['Stocks', 'Bonds', 'Real Estate', 'Commodities']
sizes = [30, 20, 25, 25]

# Create a new figure
fig = plt.figure(figsize=(6.0, 6.0))

# Plot a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Set title
plt.title('Investment Portfolio')

# Show the plot
plt.show()
```