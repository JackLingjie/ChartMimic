```python
import matplotlib.pyplot as plt  
import seaborn as sns  
import pandas as pd  

# Sample data  
d_mean = {'MAPE': [100*i for i in ([0.1674891 , 0.14371818, 0.12273398, 
       0.16679492, 0.13970324, 0.1015513 ,
       0.16319497, 0.12743953, 0.06931147]+[0.51141972, 0.51385324, 0.51403695,
       0.52769436, 0.51004928, 0.51341036, 
       0.53446   , 0.52250617, 0.5075517  ])]+[15.29211367, 14.14405139, 14.05101411]+[12.61702118, 10.50428435,  9.82247402]+[10.31754068,  7.2084087 ,  4.77361639]+[16.35151345, 16.9359747 , 17.78217523]+[14.38362791, 14.93895699, 15.7100954 ]+[13.14528142, 13.4672431 , 14.25780018], 'distribution': ['Gamma']*18+['Lognormal']*18,'inference':['ML']*9+['MOM']*9+['ML']*9+['MOM']*9}
df_mean = pd.DataFrame(data=d_mean)

# Create the figure  
fig = plt.figure(figsize=(3.54, 3.54))  
ax = fig.add_subplot(111)  
my_pal = {"ML": "#2463A3", "MOM": "#B5520E"}  
sns.violinplot(x="distribution", y="MAPE", hue="inference", data=df_mean, palette=my_pal, ax=ax)  

# Set labels  
ax.set_ylabel('MAPE (mean) %')  
ax.set_xlabel('')  

# Remove legend  
ax.get_legend().remove()  

# Despine the plot  
sns.despine()  

# Show the plot  
plt.show()
```