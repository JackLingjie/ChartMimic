```python
import numpy as np  
import matplotlib.pyplot as plt  

# Sample data  
Species = ('Iris setosa', 'Iris versicolor', 'Iris virginica', 'Iris data')  
MSL = [5.1, 5.9, 6.5, 5.8]  # Example mean sepal lengths  
y_pos = np.arange(len(Species))  

# Create a new figure  
fig = plt.figure(figsize=(6.0, 4.0))  

# Create bar plot for Mean Sepal Lengths  
plt.bar(y_pos, MSL, align='center', alpha=0.5, color='red')  
plt.xticks(y_pos, Species)  
plt.ylabel('cm')  
plt.title('Mean Sepal Lengths')  

# Show the plot  
plt.show()
```