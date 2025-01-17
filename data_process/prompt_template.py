prompt_template = """  
Please modify the following code according to these requirements:  
1. Retain only the plotting code and necessary imports; keep only matplotlib and numpy-related libraries. Do not use os, sys, or similar libraries.  
2. Avoid using custom functions or classes. Provide sequential code for plotting. If the original code is too complex or lacks plotting code, provide a new example using matplotlib.  
3. Set the figure size to `figsize=(width, height)`.  
4. Convert all text to English; do not add font settings.  
5. If multiple plots exist, retain only one.  
6. Use `plt.show()` to display the plot.  
7. Remove non-English text, path information, and initial comments from the code. Ensure the output format matches the example.  
8. Classify the resulting plot into one of the following categories: Bar, Line, ErrorBar, Heatmap, Box, Scatters, Hist, Radar, 3D, Pie, ErrorPoint, Violin, Area, Contour, Density, Graph, Quiver, Treemap, Combination, HR, Multidiff, PIP.  
9. Output the image dimensions as `(width, height)`.   
  
Please follow the reference code format for modification:  
  
{RAW_CODE}  
  
Reference output format:  
  
<REVISED CODE BEGIN>  
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  
import numpy as np  
  
# Sample data  
targets = np.array([  
    [0.2, 0.4, 0.0],  
    [0.3, 0.5, 0.2],  
    [0.4, 0.6, 0.4],  
    [0.5, 0.7, 0.6],  
    [0.6, 0.8, 0.8],  
    [0.7, 0.9, 1.0],  
    [0.8, 1.0, 1.2],  
    [0.9, 1.1, 1.4]  
])  
  
# Create a new figure  
fig = plt.figure(figsize=(7.0, 7.0))  
ax = fig.add_subplot(111, projection='3d')  
  
# Plot the targets  
ax.plot(targets[:, 0], targets[:, 1], targets[:, 2], 'o-', color='orange', label='Targets')  
  
# Set labels  
ax.set_xlabel('X')  
ax.set_ylabel('Y')  
ax.set_zlabel('Z')  
  
# Add a legend  
ax.legend()  
  
# Show the plot  
plt.show()  
<REVISED CODE END>  
  
<CATEGORY>: [Line]  
<CHART SIZE>: (7.0, 7.0)  
"""  