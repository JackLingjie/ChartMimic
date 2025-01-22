```python
import matplotlib.pyplot as plt  
import numpy as np  
from math import pi  

data1 = (8.5, 8.2, 7.7, 7.8, 7.9, 8.4, 8.1, 8.3, 8.1, 8.1, 10.0, 8.5)  
labels = ("Aries", "Pisces", "Aquarius", "Capricorn", "Sagittarius", "Scorpio",  
          "Libra", "Virgo", "Leo", "Cancer", "Gemini", "Taurus")  

N = len(labels)  
x_as = [n / float(N) * 2 * pi for n in range(N)]  

data1 += data1[:1]  
x_as += x_as[:1]  

fig = plt.figure(figsize=(6.0, 6.0))  
ax = plt.subplot(111, polar=True)  

ax.set_theta_offset(pi / 2)  
ax.set_theta_direction(-1)  

ax.set_rlabel_position(0)  

ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)  
ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)  

plt.xticks(x_as[:-1], [])  
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"])  

ax.plot(x_as, data1, linewidth=0, linestyle='solid', zorder=3, label='Data 1')  
ax.fill(x_as, data1, 'b', alpha=0.3)  

plt.ylim(0, 10)  

for i in range(N):  
    angle_rad = i / float(N) * 2 * pi  
    if angle_rad == 0:  
        ha, distance_ax = "center", 10  
    elif 0 < angle_rad < pi:  
        ha, distance_ax = "left", 1  
    elif angle_rad == pi:  
        ha, distance_ax = "center", 1  
    else:  
        ha, distance_ax = "right", 1  

    ax.text(angle_rad, 10 + distance_ax, labels[i],  
            size=10, horizontalalignment=ha, verticalalignment="center")  

plt.show()
```