```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data for two triangles
E = np.array([[0, 1, 2], [0, 2, 3]])
V = np.array([
    [0.0, 0.0],
    [1.0, 0.5],
    [1.5, -1.5],
    [-1.5, -1.5]
])

halfL = max(V[:, 0])

plt.figure(figsize=(6.4, 4.8))
for k in range(len(E)):
    N = E[k,:]
    x = V[N,0]
    y = V[N,1]
    
    x = np.append(x,x[0])  
    y = np.append(y,y[0])
    
    plt.plot(x,y,'k-')

plt.gca().set_aspect('equal')
plt.axis([-halfL-1, halfL+1,-halfL-2 , halfL])
plt.title('Mesh Visualization')
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([-halfL-1 , 0 , halfL+1])
plt.yticks([-halfL-2 , -halfL//2 , halfL ])
plt.tight_layout()
# Show the plot
plt.show()
```