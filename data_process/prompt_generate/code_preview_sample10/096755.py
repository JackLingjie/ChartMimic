```python
import matplotlib.pyplot as plt

# Create a new figure with specified size
plt.figure(figsize=(6.0, 6.0))

# Draw vector using quiver
plt.quiver(0, 0, 4, 5, angles='xy', scale_units='xy', scale=1, color='#FF0000')

# Set labels and title in English
plt.xlabel('x')
plt.ylabel('y')
plt.title('Coordinate')

# Enable grid and set aspect ratio to equal for proper scaling of plot
plt.grid(True)
axes = plt.gca()
axes.set_aspect('equal')

# Set axis limits
axes.set_xlim(-2, 10)
axes.set_ylim(-2, 10)

# Display the plot
plt.show()
```