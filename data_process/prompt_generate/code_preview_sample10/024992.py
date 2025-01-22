```python
import matplotlib.pyplot as plt  

# Sample data
sizes = [30, 20, 50]
colors = ['green', 'red', 'grey']
labels = ['Positive', 'Negative', 'Neutral']

# Create a new figure
fig = plt.figure(figsize=(6.0, 6.0))

# Plot the pie chart
plt.pie(
    x=sizes,
    shadow=True,
    colors=colors,
    labels=labels,
    startangle=90
)

# Set the title
plt.title("Sentiment of Tweets")

# Show the plot
plt.show()
```