```python
import matplotlib.pyplot as plt  
import numpy as np  

# Data  
temp = [-60., 20., 90.]  
impact_energy_al = [9.932, 8.126, 9.932]  

# Create a new figure  
plt.figure(figsize=(7.0, 5.0))  

# Plot the data  
plt.plot(temp, impact_energy_al, 'k.', label='Aluminium')  

# Set labels  
plt.xlabel('Temperature (°C)')  
plt.ylabel('Impact energy K (J)')  

# Add a legend  
plt.legend()  

# Show the plot  
plt.show()
```