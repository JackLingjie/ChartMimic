```python
import matplotlib.pyplot as plt
import seaborn as sb

# Load the Iris dataset
IrisData = sb.load_dataset('iris')

# Set the figure size
plt.figure(figsize=(7.0, 5.0))

# Create a violin plot
sb.violinplot(x='species', y='sepal_width', data=IrisData)

# Show the plot
plt.show()
```