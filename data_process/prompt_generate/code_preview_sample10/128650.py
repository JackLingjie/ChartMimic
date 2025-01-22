```python
import matplotlib.pyplot as plt  
import networkx as nx  

# Create a simple graph
G = nx.Graph()
edges = [((0, 0), (1, 1)), ((1, 1), (2, 2)), ((2, 2), (3, 3))]
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(6.0, 4.0))
pos = {n: n for n in G.nodes}
nx.draw(G, pos=pos, with_labels=True)

# Display the plot
plt.show()
```