```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
labels = ['Paint', 'Put', 'Grasp', 'Move', 'Hide', 'Make', 'Throw', 'Turn on', 'Turn off', 'Open', 'Close']
sizes = np.array([10, 20, 15, 25, 5, 30, 10, 5, 5, 10, 15])
explode = (0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01)
textprops = {'fontsize': 16}
percent = 100. * sizes / sizes.sum()

plt.figure(figsize=(7.5, 5))
patches, text = plt.pie(sizes, explode=explode, labels=labels, labeldistance=1.1, shadow=False, startangle=90, textprops=textprops)

labels = ['{0} - {1:1.2f} %'.format(i, j) for i, j in zip(labels, percent)]
plt.legend(patches, labels, loc='best', fontsize=16)
plt.axis('equal')
plt.show()
```