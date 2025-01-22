```python
import matplotlib.pyplot as plt  
import numpy as np  
import pandas as pd  
import seaborn as sns  

# Sample data  
data = {'weather': ['sunny', 'cloudy', 'rainy', 'sunny', 'cloudy', 'rainy'],  
        'sales': [200, 150, 100, 220, 160, 110]}  
df = pd.DataFrame(data)  

# Violin plot  
plt.figure(figsize=(6.0, 4.0))  
sns.violinplot(x='weather', y='sales', data=df)  
plt.xlabel('Weather')  
plt.ylabel('Sales')  
plt.title('Sales by Weather')  
plt.show()
```