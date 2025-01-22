```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
cov_epi = np.array([0.0, 0.05, 0.1, 0.15, 0.2])
mean_episize = np.array([600, 580, 560, 540, 520])
episize_sd = np.array([10, 15, 20, 25, 30])

# Plot episize by vax coverage
plt.figure(figsize=(6.0, 4.0))
plt.errorbar(cov_epi, mean_episize, yerr=episize_sd, color='black', linestyle='None', marker='o')
plt.xlabel('Proportion of vax coverage')
plt.ylabel('Epidemic size')
plt.xlim([0, 0.25])
plt.show()
```