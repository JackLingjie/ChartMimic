```python
import matplotlib.pyplot as plt  
import numpy as np  

# Data
N = [256, 512]
Nplus = [64, 128, 256, 512]
discont_mean_data = np.array([4.33, 2.39, 1.67, 0.97])
discont_mean_data_w5 = np.array([4.1, 2.21, 1.58, 0.95])
discont_mean_RE = np.array([1.67, 0.97])
discont_mean_RE_w5 = np.array([1.58, 0.95])

# Plot
plt.figure(figsize=(7.0, 5.0))
plt.loglog(Nplus, discont_mean_data, '.', linestyle='solid', c='blue', label="Discont., mean (d)", base=2)
plt.loglog(Nplus, discont_mean_data_w5, '.', linestyle='dashed', c='blue', label="Discont., mean (d+W5)", base=2)
plt.loglog(N, discont_mean_RE, '.', linestyle='dotted', c='blue', label="Discont., mean (RE)", base=2)
plt.loglog(N, discont_mean_RE_w5, '.', linestyle='dashdot', c='blue', label="Discont., mean (RE+W5)", base=2)

plt.legend()
plt.grid(which='major', linestyle='-')
plt.grid(which='minor', linestyle='--', linewidth='0.2')
plt.xlabel("N")
plt.ylabel("L1 error (% of GT)")
plt.title("Richardson Extrapolation: Discontinuous Shear Layer, Mean")

plt.show()
```