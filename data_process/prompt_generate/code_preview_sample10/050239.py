```python
import matplotlib.pyplot as plt  
import networkx as nx  

# Create a graph  
G = nx.Graph()  
nodes = ["Karen", "J6", "Gitaru", "J1", "J4", "J7"]  
G.add_nodes_from(nodes)  

# Add edges and their weights  
G.add_edge("Karen", "J1", weight="2.8")  
G.add_edge("Karen", "J6", weight="4")  
G.add_edge("J1", "J4", weight="2.6")  
G.add_edge("J6", "Gitaru", weight="10")  
G.add_edge("J6", "J7", weight="6")  
G.add_edge("J6", "J4", weight="6")  
G.add_edge("Gitaru", "J7", weight="6")  

# Position the nodes  
G.nodes["Karen"]['pos'] = (0, 0)  
G.nodes["J6"]['pos'] = (0, 2)  
G.nodes["J1"]['pos'] = (2, -2)  
G.nodes["J4"]['pos'] = (4, -2)  
G.nodes["J7"]['pos'] = (0, 4)  
G.nodes["Gitaru"]['pos'] = (-1, 3)  

# Store all positions in a variable  
node_pos = nx.get_node_attributes(G, 'pos')  

# Get edge weights  
arc_weight = nx.get_edge_attributes(G, 'weight')  

# Draw the graph  
plt.figure(figsize=(7.0, 7.0))  
nx.draw_networkx(G, node_pos, node_size=450, node_color='darkturquoise')  
nx.draw_networkx_edges(G, node_pos, width=2, edge_color='darkturquoise')  
nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)  
plt.axis('off')  
plt.show()
```