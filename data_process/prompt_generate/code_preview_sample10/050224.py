```python
import matplotlib.pyplot as plt

# Data
edu = [0.2515, 0.3724, 0.3336, 0.0368, 0.0057]
labels = ['Vocational', 'Associate', 'Bachelor', 'Master', 'Other']

# Create a new figure
plt.figure(figsize=(6.0, 6.0))

# Plot a pie chart
plt.pie(x=edu, labels=labels, autopct='%.1f%%')

# Show the plot
plt.show()
```