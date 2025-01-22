```python
import matplotlib.pyplot as plt

# Data
type = ('AD', 'NC')
y_pred = (0.78, 0.22)

# Create a new figure
fig, ax = plt.subplots(1, 1, figsize=(7.0, 5.0))
ax.set_xlim([0.0, 1.0])
ax.set_xlabel('Prediction Accuracy')

# Plot the data
h = ax.barh(type, y_pred, color=['salmon', 'skyblue'])

# Add legend and annotations
plt.legend(h,type)
for p in ax.patches:
    percentage = '{:.2f}%'.format(100 * p.get_width())
    x = p.get_x() + p.get_width() + 0.02
    y = p.get_y() + p.get_height()/2
    ax.annotate(percentage, (x,y), fontsize=10)

# Show the plot  
plt.show()
```