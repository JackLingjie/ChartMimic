```python
import matplotlib.pyplot as plt  
import pandas as pd  

# Sample data creation (as the original data import is not allowed)
data = pd.DataFrame({'Age': [22, 38, 26, 35, 28]})

# Plot 'Age' variable in a histogram
plt.figure(figsize=(6.0, 4.0))  
plt.hist(data['Age'], bins=10, color='blue', edgecolor='black')  
plt.xlabel('Age (years)')  
plt.ylabel('Count')  

# Show the plot
plt.show()
```