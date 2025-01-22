```python
import matplotlib.pyplot as plt  
from matplotlib.patches import Rectangle  
import numpy as np  

# Sample data
data = ['apple', 'banana', 'apricot', 'blueberry'] 
colormap = {'a': 'red', 'b': 'blue'}

# Initialize the plot
fig, ax = plt.subplots(figsize=(6.0, 4.0))

# Plotting logic
y_offset = 0
for item in data:
    char_counter = {}
    for char in item:
        if char not in colormap:
            continue
        count = char_counter.get(char, 0) + 1
        ax.add_patch(Rectangle((count-1, y_offset), 1, 1, color=colormap[char]))
        char_counter[char] = count

    y_offset += 1

ax.set_xlim(0, max(len(s) for s in data))
ax.set_ylim(0, len(data))

# Show the plot  
plt.show()
```