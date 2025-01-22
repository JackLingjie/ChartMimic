```python
import matplotlib.pyplot as plt  
import numpy as np  

# Sample data
bases_pos = [[1, 2], [5, 1], [5, 4], [10, 4], [2, 6], [5, 8]]
agents_pos = [[2, 1], [4, 6], [7, 1]]
delivery_pos = [0, 4]

# Create a new figure
fig = plt.figure(figsize=(7.0, 7.0))
ax = fig.add_subplot(111)

# Set grid and ticks
ax.set_xticks(np.arange(0, 11))
ax.set_yticks(np.arange(0, 11))
plt.grid()

# Plot bases
for base_pos in bases_pos:
    plt.scatter(base_pos[0], base_pos[1], marker='s', s=1000, c='#dddddd')

# Plot deliveries
for d in range(len(delivery_pos)):
    plt.scatter(bases_pos[delivery_pos[d]][0], bases_pos[delivery_pos[d]][1], marker='o', c='#000000', s=100, label='Delivery' if d == 0 else None)

# Plot agents
for agent_pos in agents_pos:
    plt.scatter(agent_pos[0], agent_pos[1], marker='s', s=100, label='Agent' if agent_pos == agents_pos[0] else None)

plt.legend()
plt.show()
```