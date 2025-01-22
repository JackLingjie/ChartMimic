```python
import matplotlib.pyplot as plt  
import numpy as np  
import seaborn as sn  

# Sample confusion matrix data  
cm = np.array([[5, 1, 0],  
               [2, 3, 1],  
               [0, 1, 4]])  

# Create a heatmap  
plt.figure(figsize=(6.0, 4.0))  
sn.heatmap(cm, annot=True, linewidths=1, cmap="YlOrRd")  
plt.xlabel('Predicted')  
plt.ylabel('True')  
plt.show()
```