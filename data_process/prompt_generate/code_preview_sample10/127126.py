```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data for radar plot
labels=np.array(['Metric 1', 'Metric 2', 'Metric 3', 'Metric 4'])
stats=np.array([20, 34, 30, 35])

angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
stats=np.concatenate((stats,[stats[0]]))
angles+=angles[:1]

fig, ax = plt.subplots(figsize=(6.0,6.0), subplot_kw=dict(polar=True))
ax.fill(angles, stats, color='red', alpha=0.25)
ax.plot(angles, stats)

# Set labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.show()
```