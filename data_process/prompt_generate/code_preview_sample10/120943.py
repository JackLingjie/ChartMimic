```python
import matplotlib.pyplot as plt
import numpy as np

# Sample error data for plotting
L2err = np.array([0.1, 0.05, 0.025, 0.0125])
h = np.array([1.0, 0.5, 0.25, 0.125])

fig, ax = plt.subplots(figsize=(6.4, 4.8)) 

# Plotting the sample error data
ax.loglog(h, L2err, 'k.', label='Results')
ax.set_xlabel('Step size $(\Delta t)$')
ax.set_ylabel('L2 Error')
ax.legend()
ax.set_title('Convergence Test')

plt.tight_layout()
plt.show()
```