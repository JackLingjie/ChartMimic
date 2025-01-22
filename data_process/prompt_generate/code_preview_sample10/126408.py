```python
import matplotlib.pyplot as plt  
import pandas as pd  

# Sample data for demonstration
data = [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]  
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(10.0, 4.5))

# Plot the box plot of the sample data
df.plot.box(title="Box plot of Sample Data")
plt.grid(linestyle="--", alpha=0.3)

# Display the plot
plt.show()
```