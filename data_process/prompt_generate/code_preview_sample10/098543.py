```python
import matplotlib.pyplot as plt  
import numpy as np  
import seaborn as sns  

# Sample data for rentals by year
years = np.array([2011, 2012])
average_rentals = np.array([4200, 4800])

# Create a new figure
plt.figure(figsize=(5, 5))  

# Plot the data using seaborn pointplot
ax = sns.pointplot(x=years, y=average_rentals, ci=95.0)

# Set plot labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Average Rentals')
plt.title('Figure: Average Rentals by Year')

# Display mean line on the graph
plt.axhline(y=np.mean(average_rentals), linewidth=1, linestyle='dashed', color="indigo")

# Show the plot
plt.show()
```