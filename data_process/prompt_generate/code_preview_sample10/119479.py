```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data for plotting
time = np.linspace(0, 10, 100)
voltage = np.sin(time)  # Example voltage data

# Create a new figure with specified size
fig = plt.figure(figsize=(6.0, 4.0))  

# Plot the voltage over time
plt.plot(time, voltage, label='Voltage over Time')  

# Set labels and title
plt.xlabel('Time (ms)')  
plt.ylabel('Voltage (mV)')  
plt.title('Membrane Potential')

# Add a legend
plt.legend()  
  
# Show the plot
plt.show()
```