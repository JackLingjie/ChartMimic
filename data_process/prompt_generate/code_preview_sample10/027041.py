```python
import matplotlib.pyplot as plt  
import seaborn as sns  
import pandas as pd  

# Sample data  
d_var = {'MAPE': [56.51961891, 50.47877742, 46.13735704, 56.41471139, 48.30979619, 39.03006257, 56.08137685, 44.53477141, 27.01354216, 287.74453306, 298.1863082, 298.21313797, 299.7961364, 300.44014621, 311.36703739, 324.08161946, 323.83104867, 327.57942772, 67.89211699, 64.24130949, 63.92732816, 60.43748406, 50.92945822, 46.84127056, 54.94239969, 39.2380389, 24.5262507, 195.21194215, 232.21351093, 238.5230456, 219.98637949, 221.72468045, 217.98143615, 226.76576441, 196.59937264, 221.02871965], 'distribution': ['Gamma']*18+['Lognormal']*18, 'inference': ['ML']*9+['MOM']*9+['ML']*9+['MOM']*9}  
df_var = pd.DataFrame(data=d_var)  

# Create the figure  
fig = plt.figure(figsize=(3.54, 3.54))  
ax = fig.add_subplot(111)  
my_pal = {"ML": "#2463A3", "MOM": "#B5520E"}  
sns.violinplot(x="distribution", y="MAPE", hue="inference", data=df_var, palette=my_pal, ax=ax)  

# Set labels  
ax.set_ylabel('MAPE (standard deviation) %')  
ax.set_xlabel('')  

# Remove legend  
ax.get_legend().remove()  

# Show the plot  
plt.show()
```