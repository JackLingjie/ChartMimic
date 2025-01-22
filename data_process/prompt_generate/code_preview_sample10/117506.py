```python
import matplotlib.pyplot as plt  
import seaborn as sns  
import pandas as pd  

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [5, 10, 15, 20]
}
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(6.0, 4.0))

# Generate a violin plot
sns.violinplot(x='Category', y='Value', data=df)

# Display the plot
plt.show()
```