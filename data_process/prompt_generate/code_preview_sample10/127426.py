```python
import matplotlib.pyplot as plt  
import seaborn as sns  
import pandas as pd  
  
# Sample DataFrame
example = {  
    "Column 1": [1, 2, 5, 3, 7],  
    "Column 2": [5, 7, 1, 2, 5],  
    "Column 3": [7, 2, 5, 4, 1],  
}  

example = pd.DataFrame(example)

# Create a violin plot
plt.figure(figsize=(6.0,4.0)) 
sns.violinplot(data=example)

# Show the plot
plt.show()
```