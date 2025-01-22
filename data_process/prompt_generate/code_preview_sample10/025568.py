```python
import numpy as np  
import matplotlib.pyplot as plt  

# Sample data  
ell = np.array([100, 200, 300, 400, 500, 600, 700, 800])  
PEE = np.array([1.0, 1.2, 1.1, 1.3, 1.5, 1.4, 1.6, 1.7])  
Ediagerr = np.array([0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2])  

# Create a new figure  
fig, ax = plt.subplots(figsize=(7.0, 5.0))  

# Plot the data  
ax.errorbar(ell, PEE, yerr=Ediagerr, fmt='o', markersize=5, color='b', label='E-mode')  

# Set labels  
ax.set_xlabel('Multipole moment $\ell$')  
ax.set_ylabel('Power Spectrum $C_\ell$')  

# Set limits  
ax.set_xscale('log')  
ax.set_xlim(100, 800)  
ax.set_ylim(0.5, 2.0)  

# Add a legend  
ax.legend()  

# Show the plot  
plt.show()
```