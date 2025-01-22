```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
versicolor_petal_length = np.array([4.7, 4.5, 4.9, 4.0, 4.6, 4.5, 4.7, 
                                    3.3, 4.6, 3.9])  

# Compute number of data points: n_data
n_data = len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins = int(np.sqrt(n_data))

# Set figure size
plt.figure(figsize=(6.0, 4.0))

# Plot the histogram
plt.hist(versicolor_petal_length, bins=n_bins)

# Label axes
plt.xlabel('Petal Length (cm)')
plt.ylabel('Count')

# Show histogram
plt.show()
```