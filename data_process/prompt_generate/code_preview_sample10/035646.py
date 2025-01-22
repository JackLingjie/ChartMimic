```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([[15, 39], [15, 81], [16, 6], [16, 77], [17, 40], [17, 76], [18, 6], [18, 94], [19, 3], [19, 72]])
y_hc = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

# Visualising the clusters
plt.figure(figsize=(7.0, 5.0))
plt.scatter(x[y_hc == 0, 0], x[y_hc == 0, 1], s=100, c='red', label='Cluster 1')
plt.title('Cluster of clients')
plt.xlabel('Annual income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
```