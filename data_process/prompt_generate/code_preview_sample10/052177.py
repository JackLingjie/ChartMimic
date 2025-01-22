```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.arange(100).reshape((10, 10))

# Create a new figure
fig = plt.figure(figsize=(4.0, 4.0))

# Display the image
plt.imshow(data)

# Show the plot
plt.show()
```