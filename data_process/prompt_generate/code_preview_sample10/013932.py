```python
import matplotlib.pyplot as plt  
import seaborn as sns  
import pandas as pd  

# Sample data
data = {'Churn': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
        'TotalCharges': [100, 200, 150, 250, 300, 350, 400, 450]}
churn = pd.DataFrame(data)

# Create a new figure
fig = plt.figure(figsize=(7.0, 7.0))

# Plot TotalCharges density
ax = sns.kdeplot(churn.TotalCharges[churn["Churn"] == 'Yes'], color="lightcoral", shade=True)
ax = sns.kdeplot(churn.TotalCharges[churn["Churn"] == 'No'], ax=ax, color="steelblue", shade=True)

# Set labels
ax.set_xlabel("Total Charges")
ax.set_ylabel("Frequency")
plt.title('Variation of "Total Charges" for [Un-]Churned customers')

# Add a legend
ax.legend(["Churned", "UnChurned"])

# Show the plot
plt.show()
```