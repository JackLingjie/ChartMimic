```python
import matplotlib.pyplot as plt  
import numpy as np  
from matplotlib.patches import Polygon  

# Colors  
lgray = "#dddddd"  # light gray  

# Range of x and y axis  
xmin_ax = -1  
xmax_ax = 2  
ymin_ax = -0.75  
ymax_ax = 1  

# Arrows head length and head width  
hl = 10  
hw = 6  
hl_ax = 8  
hw_ax = 4  

fig = plt.figure(figsize=(4, 3))  
ax = plt.subplot2grid((1, 8), (0, 0), rowspan=1, colspan=8)  

plt.xlim(xmin_ax, xmax_ax)  
plt.ylim(ymin_ax, ymax_ax)  

# x axis  
plt.annotate("", xytext=(0, 0), xycoords='data', xy=(xmax_ax, 0), textcoords='data',  
             arrowprops=dict(width=0.01, headwidth=hw_ax, headlength=hl_ax, facecolor='black', shrink=0.002))  
# z axis  
plt.annotate("", xytext=(0, 0), xycoords='data', xy=(0, ymax_ax), textcoords='data',  
             arrowprops=dict(width=0.01, headwidth=hw_ax, headlength=hl_ax, facecolor='black', shrink=0.002))  
# y axis  
y_e = -0.6  
plt.annotate("", xytext=(0, 0), xycoords='data', xy=(xmin_ax, y_e), textcoords='data',  
             arrowprops=dict(width=0.01, headwidth=hw_ax, headlength=hl_ax, facecolor='black', shrink=0.002))  

# Slope of the y axis  
p = (0 - y_e) / (0 - xmin_ax)  

# x1 vector  
x1_x = 0.6  
x1_y = 0  
plt.annotate("", xytext=(0, 0), xycoords='data', xy=(x1_x, x1_y), textcoords='data',  
             arrowprops=dict(width=1, headwidth=hw, headlength=hl, facecolor='black', shrink=0.002))  
# x2 vector  
x2_x = -0.4  
x2_y = p * x2_x  
plt.annotate("", xytext=(0, 0), xycoords='data', xy=(x2_x,  x2_y), textcoords='data',  
             arrowprops=dict(width=1, headwidth=hw, headlength=hl, facecolor='black', shrink=0.002))  

s_x = 0.9  
s_y = 0.75  
# s vector  
plt.annotate("", xytext=(0, 0), xycoords='data', xy=(s_x, s_y), textcoords='data',  
             arrowprops=dict(width=1, headwidth=hw, headlength=hl, facecolor='black', shrink=0.002))  
# s projection  
sp_x = s_x  
sp_y = -0.4  
plt.annotate("", xytext=(0, 0), xycoords='data', xy=(sp_x, sp_y), textcoords='data',  
             arrowprops=dict(width=1, headwidth=hw, headlength=hl, facecolor='black', shrink=0.002))  

# sp to s arrow  
plt.annotate("", xytext=(sp_x, sp_y), xycoords='data', xy=(s_x, s_y), textcoords='data',  
             arrowprops=dict(width=1, headwidth=hw, headlength=hl, facecolor='black', shrink=0.002))  

# Shaded region  
px1 = 0.9  
py1 = -0.5  
px2 = 1.85  
py2 = p * (px2 - px1) + py1  
px4 = -1  
py4 = py1  
py3 = py2  
px3 = (py3-py4) / p + px4  
vertices = np.array([[px1, py1], [px2, py2], [px3, py3], [px4, py4]])  
ax.add_patch(Polygon(vertices, facecolor=lgray, edgecolor='none'))  

plt.axis('off')  

plt.show()
```