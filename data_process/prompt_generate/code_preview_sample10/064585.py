```python
import matplotlib.pyplot as plt  
import numpy as np  
import seaborn as sns  

# Sample data  
avgArr6 = [102.4, 102.4, 102.4, 204.8, 204.8, 204.8, 307.2, 307.2, 409.6, 512.0, 614.4, 716.8]  
avgArr14 = [512.0, 614.4, 716.8, 819.2, 921.6, 1024.0, 1126.4, 1228.8, 1331.2, 1536.0, 1638.4]  
avgArr25 = [1331.2, 1638.4, 1740.8, 1843.2, 1945.6, 2048.0, 2150.4, 2252.8, 2355.2, 2457.6, 2560.0]  

a6 = np.array(avgArr6)  
a14 = np.array(avgArr14)  
a25 = np.array(avgArr25)  

sns.set(style="white", palette="muted", color_codes=True)  

# Create a new figure  
plt.figure(figsize=(7.0, 7.0))  

# Plot the distributions  
sns.distplot(a6, color="#4285f4", label='6 stations')  
sns.distplot(a14, color="#ea4335", label='14 stations')  
sns.distplot(a25, color="#fbbc04", label='25 stations')  

# Add a legend  
plt.legend()  

# Show the plot  
plt.show()
```