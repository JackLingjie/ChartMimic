```python
import numpy as np  
import matplotlib.pyplot as plt  

# Sample data  
iptg = np.array([0.001, 0.01, 0.1, 1, 10])  
gfp = np.array([0.1, 0.4, 0.6, 0.8, 0.9])  
sem = np.array([0.01, 0.02, 0.03, 0.02, 0.01])  

# Create a new figure  
plt.figure(figsize=(6.0, 4.0))  

# Plot with error bars  
plt.errorbar(iptg, gfp, yerr=sem, linestyle='none', marker='.', markersize=20)  
plt.title('IPTG Titration - semilog X')  
plt.xlabel('IPTG (mM)')  
plt.ylabel('Normalized GFP')  
plt.ylim(-0.02, 1.02)  
plt.xlim(8e-4, 15)  
plt.xscale('log')  

# Show the plot  
plt.show()
```