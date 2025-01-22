```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data  
input_data = np.array([  
    [0.88, 0.44, 0.14, 0.16, 0.37, 0.77, 0.96, 0.27],  
    [0.19, 0.45, 0.57, 0.16, 0.63, 0.29, 0.71, 0.70],  
    [0.66, 0.26, 0.82, 0.64, 0.54, 0.73, 0.59, 0.26],  
    [0.85, 0.34, 0.76, 0.84, 0.29, 0.75, 0.62, 0.25],  
    [0.32, 0.74, 0.21, 0.39, 0.34, 0.03, 0.33, 0.48],  
    [0.20, 0.14, 0.16, 0.13, 0.73, 0.65, 0.96, 0.32],  
    [0.19, 0.69, 0.09, 0.86, 0.88, 0.07, 0.01, 0.48],  
    [0.83, 0.24, 0.97, 0.04, 0.24, 0.35, 0.50, 0.91],  
], dtype=np.float32)  

# Create a new figure  
fig = plt.figure(figsize=(6.0, 4.0))  

# Display the input data as an image  
plt.imshow(input_data, cmap='jet', interpolation='nearest')  
plt.title('Input Data')  

# Show the plot  
plt.show()
```