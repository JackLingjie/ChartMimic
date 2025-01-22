```python
import matplotlib.pyplot as plt
from sklearn import tree
import numpy as np

# Sample data
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = np.array([[36, 10, 9, 0],
              [42, 12, 4, 1],
              [23, 4, 6, 2],
              [52, 4, 4, 1],
              [43, 21, 8, 1],
              [44, 14, 5, 0]])
y = np.array([0, 0, 1, 1, 1, 0])

# Train a decision tree classifier
dtree = tree.DecisionTreeClassifier()
dtree.fit(X, y)

# Plot the decision tree
fig, ax = plt.subplots(figsize=(6.0, 6.0))
tree.plot_tree(dtree, feature_names=features, class_names=['NO', 'GO'], filled=True, ax=ax)

# Show the plot
plt.show()
```