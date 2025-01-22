```python
import matplotlib.pyplot as plt

# Sample data
list1 = [1.0, 2.0, 3.0, 4.0]
list2 = [5.0, 6.5, 7.8, 9.1]
data = [list1, list2]

# Create a new figure with specified size
fig = plt.figure(figsize=(6.4, 4.8))
axes = fig.add_subplot(111)

# Configure the boxplot
axes.set_ylabel('Runtime in msec (log scale)')
axes.set_yscale('log')
axes.boxplot(data, patch_artist=True, labels=['DUCKDB', 'GRainDB'], showmeans=False)

# Display the plot
plt.show()
```