```python
import matplotlib.pyplot as plt  
import numpy as np  

# Generate sample data
sample_space_10 = {0: 1, 1: 10, 2: 45, 3: 120, 4: 210, 
                   5: 252, 6:210,7:120 ,8 :45 ,9 :10 ,10 :1}
sample_space_10_size = sum(sample_space_10.values())
head_counts = list(sample_space_10.keys())
probability_of_x_heads = [sample_space_10[key]/sample_space_10_size for key in head_counts]

# Create a new figure with specified size
plt.figure(figsize=(6.0,4.0))

# Plot the data
plt.scatter(head_counts, probability_of_x_heads)
plt.plot(head_counts, probability_of_x_heads)

# Highlight area between plots where condition is met (in this case just to show functionality)
where = [value <3 or value >7 for value in head_counts]
plt.fill_between(head_counts,
                 probability_of_x_heads,
                 where=where,
                 color='gray', alpha=0.5)

# Set labels
plt.xlabel("Count of heads")
plt.ylabel("Probability x heads")

# Show the plot
plt.show()
```