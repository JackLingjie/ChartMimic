```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data  
bore_string = '''
7.978
7.967
7.965
7.968
7.968
7.968
7.981
7.977
7.97
7.978
7.967
7.964
7.968
7.981
7.971
7.977
7.972
7.976
7.971
7.974
7.976
7.976
7.973
7.962
7.972
7.988
7.983
7.976
7.967
7.978
7.974
7.956
7.98
7.981
7.978
7.974
'''

bores = [float(x) for x in bore_string.split()]

# Create a new figure
plt.figure(figsize=(6.0, 4.0))

# Plot the histogram
plt.hist(bores, rwidth=0.9)

# Set title
plt.title("Sun gear bore tolerance")

# Show the plot
plt.show()
```