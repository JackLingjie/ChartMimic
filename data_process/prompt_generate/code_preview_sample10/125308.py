```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure(figsize=(6.0, 4.0))
G = gridspec.GridSpec(3, 3)

axes_1 = plt.subplot(G[0, :])
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=24, alpha=.5)

plt.tight_layout()
plt.show()
```