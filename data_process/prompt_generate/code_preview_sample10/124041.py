```python
import matplotlib.pyplot as plt  
import seaborn as sb  

# Load Iris dataset
IrisData = sb.load_dataset('iris')

# Set the figure size
plt.figure(figsize=(6.0, 4.0))

# Plot kernel density estimation of sepal_width
sb.kdeplot(IrisData['sepal_width'], shade=True)

# Show the plot
plt.show()
```