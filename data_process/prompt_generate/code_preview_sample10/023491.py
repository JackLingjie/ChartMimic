```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
eigenvalues_f = np.array([1+2j, 2+3j, 3-1j, 4-2j])
eigenvalues_a = np.array([1.5+2.5j, 2.5+3.5j, 3.5-1.5j, 4.5-2.5j])

# Create a new figure
fig = plt.figure(figsize=(4.5, 6))  
ax = fig.add_subplot(111)  

# Plot numerical eigenvalues
for i in range(len(eigenvalues_f)):
    if eigenvalues_f[i].imag > 0:
        ax.plot(eigenvalues_f[i].real, eigenvalues_f[i].imag, 'b^', markersize=5, label='Acc. Down' if i == 0 else "")
    elif eigenvalues_f[i].imag < 0:
        ax.plot(eigenvalues_f[i].real, eigenvalues_f[i].imag, 'bs', markersize=5, label='Acc. Up' if i == 0 else "")

# Plot analytical eigenvalues
ax.plot(eigenvalues_a.real, eigenvalues_a.imag, 'ko', markerfacecolor='None', markersize=10, label='Analytical')

# Set labels
ax.set_xlabel('Re(k_z)', fontsize=12)
ax.set_ylabel('Im(k_z)', fontsize=12)

# Add a legend
ax.legend(numpoints=1)

# Show the plot
plt.show()
```