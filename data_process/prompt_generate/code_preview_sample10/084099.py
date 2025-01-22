```python
import matplotlib.pyplot as plt  
import numpy as np  

# Define colors for corners
topLeft = [0, 0, 0]
topRight = [255, 0, 0]
bottomLeft = [0, 255, 0]
bottomRight = [0, 0, 255]

resolution = 4

# Create gradients for each side
redVerticalLeft = np.linspace(topLeft[0], bottomLeft[0], resolution)
greenVerticalLeft = np.linspace(topLeft[1], bottomLeft[1], resolution)
blueVerticalLeft = np.linspace(topLeft[2], bottomLeft[2], resolution)

redVerticalRight = np.linspace(topRight[0], bottomRight[0], resolution)
greenVerticalRight = np.linspace(topRight[1], bottomRight[1], resolution)
blueVerticalRight = np.linspace(topRight[2], bottomRight[2], resolution)

# Initialize the image array
resultImage = np.zeros((resolution, resolution, 3), dtype=np.uint8)

# Fill the image with interpolated colors
for indexRow in range(resolution):
    redHorizontal = np.linspace(redVerticalLeft[indexRow], redVerticalRight[indexRow], resolution)
    greenHorizontal = np.linspace(greenVerticalLeft[indexRow], greenVerticalRight[indexRow], resolution)
    blueHorizontal = np.linspace(blueVerticalLeft[indexRow], blueVerticalRight[indexRow], resolution)

    for indexCol in range(resolution):
        resultImage[indexRow, indexCol, :] = [redHorizontal[indexCol], greenHorizontal[indexCol], blueHorizontal[indexCol]]

# Plot the image
plt.figure(figsize=(6.0, 6.0))
plt.imshow(resultImage)
plt.axis('off')
plt.show()
```