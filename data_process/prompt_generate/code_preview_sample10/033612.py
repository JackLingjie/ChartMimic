```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
avg_overall_strategy_list = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
action_std = np.array([0.05, 0.04, 0.03, 0.02, 0.01, 0.02])

# Create a new figure
plt.figure(figsize=(6.0, 4.0))

# Plot the error bar
plt.errorbar(x=range(6), y=avg_overall_strategy_list, yerr=action_std, label="Averaged proportion of EQW over 10 runs")
plt.ylabel("Frequency")
plt.xlabel("Block number")
plt.legend()

# Show the plot
plt.show()
```