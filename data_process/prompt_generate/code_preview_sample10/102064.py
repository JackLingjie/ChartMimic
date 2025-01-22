```python
import matplotlib.pyplot as plt
import numpy as np

# Parameters for ellipse
xcenter, ycenter = 0.38, 0.52
width, height = 0.1, 0.3
angle = -30

# Calculate the theta values for the ellipse outline
theta = np.arange(0.0, 360.0, 1.0) * np.pi / 180.0
x = 0.5 * width * np.cos(theta)
y = 0.5 * height * np.sin(theta)

# Rotation matrix to rotate the ellipse by 'angle'
rtheta = angle * np.pi / 180.
R = np.array([
    [np.cos(rtheta), -np.sin(rtheta)],
    [np.sin(rtheta), np.cos(rtheta)],
])

x_rotated, y_rotated = np.dot(R, np.array([x, y]))
x_rotated += xcenter
y_rotated += ycenter

# Create a new figure with specified size
fig = plt.figure(figsize=(6., 4.))

ax = fig.add_subplot(111)
ax.fill(x_rotated, y_rotated, alpha=0.2, facecolor='yellow', edgecolor='yellow', linewidth=1)

plt.show()
```