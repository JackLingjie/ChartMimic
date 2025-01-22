```python
import matplotlib.pyplot as plt

# Data for the pie chart
slices = [50, 20, 15, 15]
depts = ['AI', 'Cloud', 'Database', 'Product Management']
cols = ['magenta', 'cyan', 'red', 'gold']

# Create a pie chart
plt.figure(figsize=(6.0, 6.0))
plt.pie(slices, labels=depts, colors=cols, startangle=90,
        explode=(0, 0.2, 0, 0), shadow=True, autopct='%.1f%%')

# Set title
plt.title('Percentage of Employees in Each Department')

# Show the pie chart
plt.show()
```