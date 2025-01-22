```python
import matplotlib.pyplot as plt  
import numpy as np  

# Create a colormap
cm_data = [
    [0.10387, 0.056805, 0.20243],
    [0.99708, 0.99733, 0.84887]
]
tokyo_map = plt.cm.colors.LinearSegmentedColormap.from_list('tokyo', cm_data)

# Sample data
data = np.linspace(0, 100, 256)[None, :]

# Create a new figure
fig = plt.figure(figsize=(6.0, 4.0))

# Display the data
plt.imshow(data, aspect='auto', cmap=tokyo_map)

# Show the plot
plt.show()
```