```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [4, 3, 2, 5]

N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6.0, 6.0), subplot_kw=dict(polar=True))

ax.plot(angles, values)
ax.fill(angles, values, alpha=0.25)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

plt.show()
```