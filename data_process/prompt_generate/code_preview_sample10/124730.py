```python
import matplotlib.pyplot as plt  
from sklearn.datasets import load_iris
import pandas as pd

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Boxplot
plt.figure(figsize=(8.0, 6.0))
df.plot(kind='box')
plt.title('Boxplot of Iris Dataset Features')
plt.ylabel('Values')
plt.xlabel('Features')

# Show the plot
plt.show()
```