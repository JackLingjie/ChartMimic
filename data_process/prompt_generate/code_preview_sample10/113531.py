```python
import matplotlib.pyplot as plt  
import pandas as pd  

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

# Box and whisker plot
fig = plt.figure(figsize=(10.0, 6.0))
dataset.plot(kind='box', subplots=False)
plt.title('Box and Whisker Plot for Iris Dataset')
plt.xlabel('Features')
plt.ylabel('Value')

# Show the plot
plt.show()
```