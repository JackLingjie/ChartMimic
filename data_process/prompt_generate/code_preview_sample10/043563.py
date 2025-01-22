```python
import matplotlib.pyplot as plt  
import matplotlib.patches as mpatches  
import matplotlib.path as mpath  

# Pairs of grid points
x = [0, 1, 2, 1, 3, 4]
y = [3, 1, 2, 4, 0, 3]

fig, ax = plt.subplots(figsize=(7.0, 7.0))

Path = mpath.Path
path_data = [
    (Path.MOVETO, (x[0], y[0])),
    (Path.LINETO, (x[1], y[1])),
    (Path.LINETO, (x[2], y[2])),
    (Path.LINETO, (x[3], y[3])),
    (Path.CLOSEPOLY, (x[0], y[0])),
    (Path.MOVETO, (x[1], y[1])),
    (Path.LINETO, (x[4], y[4])),
    (Path.LINETO, (x[5], y[5])),
    (Path.LINETO, (x[2], y[2])),
    (Path.CLOSEPOLY, (x[1], y[1])),
    (Path.MOVETO, (x[2], y[2])),
    (Path.LINETO, (x[5], y[5])),
    (Path.LINETO, (x[3], y[3])),
    (Path.CLOSEPOLY, (x[2], y[2])),
]
codes, verts = zip(*path_data)
path = Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='gray', alpha=0.25)
ax.add_patch(patch)

# Plot control points and connecting lines
vx, vy = zip(*path.vertices)
ax.plot(vx, vy, 'go-')

ax.grid(alpha=0.5)
ax.axis('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xticks(list(range(-1, 6)))
ax.set_yticks(list(range(-1, 6)))

plt.show()
```