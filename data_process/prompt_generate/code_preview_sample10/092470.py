```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data  
x = np.linspace(0, 10, 100)  
y = np.sin(x)  

# Create a new figure  
fig = plt.figure(figsize=(6.0, 4.0))  
plt.plot(x, y, label='Sine Wave')  

# Set labels  
plt.xlabel('X')  
plt.ylabel('Y')  
plt.title('Sine Wave Plot')  

# Add a legend  
plt.legend()  

# Show the plot  
plt.show()
```