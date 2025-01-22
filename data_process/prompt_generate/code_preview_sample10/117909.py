```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data creation for demonstration purpose
data = {'Condition': ['High reward', 'Low reward', 'High reward', 'Low reward'],
        'age_group': ['CH', 'YA', 'OA', 'CH'],
        'pers': [0.3, 0.5, 0.4, 0.6]}

df = pd.DataFrame(data)

# Set color palette
colors = ["#92e0a9", "#6d6192", "#352d4d"]
sns.set_palette(sns.color_palette(colors))

# Create a new figure with specific size
fig = plt.figure(figsize=(7.5, 7.5))

# Boxplot of Perseveration frequency by Condition and age_group
ax_00 = fig.add_subplot(111)
sns.boxplot(x='Condition', hue='age_group', y='pers',
            data=df, notch=False,
            showfliers=False,
            linewidth=0.8,
            width=0.4,
            boxprops=dict(alpha=1),
            ax=ax_00)
ax_00.set_ylabel('Estimated perseveration probability')
ax_00.set_xticklabels(['High Reward', 'Low Reward'])

plt.show()
```