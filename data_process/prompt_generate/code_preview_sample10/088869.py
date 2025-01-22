```python
import matplotlib.pyplot as plt

# Data to plot
funding_goal = 11500
labels = ['Payment to Artists', 'Kickstarter fee', 'Payment processing fees', 'Printing and Shipping']
sizes = [5960, funding_goal * 0.05, 410.2, 4442]
colors = ['forestgreen', 'gold', 'yellow', 'yellowgreen']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Create a new figure
plt.figure(figsize=(6.0, 6.0))

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=0)

plt.axis('equal')
plt.tight_layout()

# Show the plot
plt.show()
```