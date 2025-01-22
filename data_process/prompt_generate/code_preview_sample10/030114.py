```python
import matplotlib.pyplot as plt
import numpy as np

x = [0.1387, 0.2691, 0.3077, 0.3625, 0.4756, 0.5039, 0.5607, 0.6468, 0.7490, 0.7881]
t = [0.8260, 1.0469, 0.7904, 0.6638, 0.1731, -0.0592, -0.2433, -0.6630, -1.0581, -0.8839]
curva = [np.sin(2 * np.pi * xi) for xi in x]

plt.figure(figsize=(6.0, 4.0))
plt.scatter(x, t)
plt.plot(x, curva, color='#17a589')
plt.xlabel('x')
plt.ylabel('t')
plt.title('Figure 1.2')
plt.show()
```