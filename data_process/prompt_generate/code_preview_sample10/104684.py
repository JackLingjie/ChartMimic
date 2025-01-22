```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
actual_y = np.array([3, 5, 7, 9])
predicted_y = np.array([2.8, 5.1, 6.9, 8.7])

# Create a new figure
plt.figure(figsize=(6.0, 6.0))  

# Scatter plot for actual vs predicted values
plt.scatter(actual_y, predicted_y)

# Plotting the identity line (y=x)
y_max = max(max(actual_y), max(predicted_y))
y_min = min(min(actual_y), min(predicted_y))
plt.plot([y_min - 0.05 * (y_max - y_min), y_max + 0.05 * (y_max - y_min)], 
         [y_min - 0.05 * (y_max - y_min), y_max + 0.05 * (y_max - y_min)], 'k-')

# Set labels and limits
plt.xlabel('Actual Y')  
plt.ylabel('Predicted Y')  
plt.xlim(y_min - 0.05 * (y_max - y_min), y_max + 0.05 * (y_max - y_min))  
plt.ylim(y_min - 0.05 * (y_max - y_min), y_max + 0.05 * (y_max - y_min))

# Show the plot
plt.show()
```