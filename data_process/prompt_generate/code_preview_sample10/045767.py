```python
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 1, 2, 3, 5]
y2 = [0, 4, 2, 6, 8]
y3 = [1, 3, 5, 7, 9]

fig, ax = plt.subplots(figsize=(7.0, 5.0))
ax.stackplot(x, y1, y2, y3, labels=["Fibonacci", "Evens", "Odds"])
ax.legend(loc='upper left')
plt.show()
```