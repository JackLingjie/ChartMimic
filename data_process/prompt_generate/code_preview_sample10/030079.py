```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data  
x = ["Males", "Females"]  
y = [71, 101]  

# Create a new figure  
plt.figure(figsize=(6.0, 4.0))  

# Plot the data  
plt.bar(x, y, width=0.5, color="orange")  

# Set title and labels  
plt.title("Gender Ratio in Ice Hockey, Canada Winter Olympics", pad=10)  
plt.ylabel("Number of Players")  
plt.xlabel("Genders")  

# Show the plot  
plt.show()
```