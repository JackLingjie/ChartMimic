```python
import matplotlib.pyplot as plt  
import numpy as np  
import networkx as nx  

# Sample data for demonstration
G = nx.Graph()
positions = {0: (0, 0), 1: (1, 1), 2: (2, 0), 3: (3, 1)}
edges = [(0, 1), (1, 2), (2, 3)]
G.add_edges_from(edges)

# Create a new figure
fig = plt.figure(figsize=(6.0, 4.0))

# Draw the graph
nx.draw(G, pos=positions, node_size=100, with_labels=True)

# Show the plot
plt.show()
```