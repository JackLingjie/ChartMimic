```python
import matplotlib.pyplot as plt  
import numpy as np  
import seaborn as sn  

# Sample confusion matrix data
confusion_matrix_ = np.array([[50, 2, 1], [4, 45, 5], [3, 5, 47]])
classes = ['COVID-19', 'Normal', 'Viral Pneumonia']

# Plotting the heatmap
plt.figure(figsize=(6.0, 6.0))
sn.heatmap(confusion_matrix_ / np.sum(confusion_matrix_), annot=True, fmt='.2%', xticklabels=classes,
           yticklabels=classes)
plt.xlabel('True classes')
plt.ylabel('Predicted classes')

# Show the plot
plt.show()
```