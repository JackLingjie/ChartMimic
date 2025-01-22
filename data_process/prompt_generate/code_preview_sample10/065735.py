```python
import numpy as np  
import matplotlib.pyplot as plt  

# Sample data  
dataset_size = [1000, 2000, 4000, 8000, 10000, 20000, 40000, 60000, 100000, 160000, 200000]  
max_re = [0.03366, 0.02, 0.01918, 0.01603, 0.01804, 0.009486, 0.008615, 0.005721, 0.005793, 0.006804, 0.00616]  
mean_re = [0.02945, 0.01684, 0.01716, 0.01313, 0.01429, 0.006746, 0.005648, 0.00353, 0.003181, 0.004529, 0.003989]  

# Convert lists to numpy arrays  
dataset_size = np.asarray(dataset_size)  
max_re = np.asarray(max_re)  
mean_re = np.asarray(mean_re)  

# Sort data  
i_sort = np.argsort(dataset_size)  
dataset_size = dataset_size[i_sort]  
max_re = max_re[i_sort]  
mean_re = mean_re[i_sort]  

# Create a new figure  
fig, ax = plt.subplots(figsize=(7.0, 5.0))  

# Plot the data  
ax.plot(dataset_size, max_re, label="Max RE")  
ax.plot(dataset_size, mean_re, "--", label="Mean RE")  

# Set labels  
plt.xlabel("Dataset Size")  
plt.ylabel("RE")  

# Add a legend  
plt.legend()  

# Add a grid  
plt.grid()  

# Show the plot  
plt.show()
```