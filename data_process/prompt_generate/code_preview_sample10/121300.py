```python
import matplotlib.pyplot as plt
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
G_nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
G_edges = [['A', 'B'], ['A', 'C'], ['B', 'D'],
           ['B', 'E'], ['C', 'F'], ['C', 'G'], 
           ['D','H'],['E','H'],
           ['E','F'],['F','I'],
           ['G','I']]
color_map = ["green", "blue", "blue", "blue", "red", 
             "blue","blue","yellow","blue"]

# Shortest path from A to H using Dijkstra's algorithm
sp_edges=[('A','B'),('B','D'),('D','H')]

edge_color_list=['grey'] * len(G_edges)
for i, edge in enumerate(G_edges):
    if (edge[0], edge[1]) in sp_edges or (edge[1], edge[0]) in sp_edges:
        edge_color_list[i] = "red"

plt.figure(figsize=(6.0, 6.0))
nx.draw(G, with_labels=True, node_color=color_map,
        edge_color=edge_color_list,node_size=800)
plt.show()
```