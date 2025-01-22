```python
import numpy as np  
import matplotlib.pyplot as plt  

# Sample data  
x = [1, 2, 3, 4, 6, 7, 8, 9, 10]  
y = [0, 0, 0, 0, 1, 1, 1, 1, 1]  

train_X = np.asarray(x)  
train_Y = np.asarray(y)  

# Create a new figure  
fig = plt.figure(figsize=(6.0, 4.0))  
plt.xlim(-1, 12)  
plt.ylim(-0.5, 1.5)  

# Scatter plot  
plt.scatter(train_X, train_Y)  

# Line plot  
s_X = np.linspace(-2, 12, 100)  
s_Y = 1/(1 + np.power(np.e, -2*(s_X - 4)))  
plt.plot(s_X, s_Y)  

# Show the plot  
plt.show()
```