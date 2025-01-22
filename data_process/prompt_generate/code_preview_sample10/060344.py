```python
import matplotlib.pyplot as plt  
import numpy as np  
import seaborn as sns  

# Sample data  
a = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9]  
b = [0, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 7, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11]  
b = [x + 5 for x in b]  

# Create a new figure  
fig, ax_hist = plt.subplots(figsize=(7.0, 5.0))  

# Plot the distributions  
sns.histplot(a, ax=ax_hist, color='blue', kde=True, label='a')  
ax_hist.axvline(np.mean(a), color='g', linestyle='--', label='mean(a)')  
ax_hist.axvline(np.median(a), color='g', linestyle='-', label='median(a)')  

sns.histplot(b, ax=ax_hist, color='orange', kde=True, label='b')  
ax_hist.axvline(np.mean(b), color='r', linestyle='--', label='mean(b)')  
ax_hist.axvline(np.median(b), color='r', linestyle='-', label='median(b)')  

# Add a legend  
plt.legend()  

# Show the plot  
plt.show()
```