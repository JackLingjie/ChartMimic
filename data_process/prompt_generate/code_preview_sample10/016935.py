```python
import matplotlib.pyplot as plt  
import squarify  

# Sample data for plotting
sizes = [50, 30, 20]
names = ['Group A', 'Group B', 'Group C']
colors = ['green', 'blue', 'grey']

# Set figure size
plt.figure(figsize=(6, 7))

# Create tree plot
squarify.plot(sizes=sizes, label=names, color=colors, alpha=0.75, pad=True)
plt.axis('off')

# Show the plot
plt.show()
```