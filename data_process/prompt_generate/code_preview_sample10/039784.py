```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
languages = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ja', 'ko', 'zh']
no_of_tweets = [120, 95, 80, 75, 60, 50, 45, 30, 25, 20]

# Create a new figure
fig = plt.figure(figsize=(6.0, 4.0))

# Plot the bar chart
plt.bar(languages, no_of_tweets)

# Set labels
plt.ylabel('Number of Tweets')
plt.xlabel('Language')
plt.title('Top Ten Users')
plt.xticks(fontsize=5, rotation=30)
plt.yticks(fontsize=5)

# Show the plot
plt.show()
```