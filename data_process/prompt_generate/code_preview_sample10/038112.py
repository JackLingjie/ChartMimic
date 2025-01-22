```python
import matplotlib.pyplot as plt  
import pandas as pd  

# Load dataset
data = {'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9],
        'sepal_width': [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1],
        'petal_length': [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5],
        'petal_width': [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1],
        'class': ['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa',
                  'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']}
dataset = pd.DataFrame(data)

# Box plot
plt.figure(figsize=(6.0, 4.0))
dataset.plot(kind='box', subplots=False)
plt.title('Box Plot of Iris Dataset Features')
plt.show()
```