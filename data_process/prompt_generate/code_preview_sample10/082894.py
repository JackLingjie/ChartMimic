```python
import matplotlib.pyplot as plt

# Data to plot
labels = 'a', 'b', 'c', 'd'
sizes = [10, 30, 120, 40]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0, 0.1, 0)

# Create a new figure
plt.figure(figsize=(6.0, 6.0))

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=10)
plt.axis('equal')

# Show the plot
plt.show()
```