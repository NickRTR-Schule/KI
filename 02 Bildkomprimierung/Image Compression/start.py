import matplotlib.image as mpimg
from matplotlib import pyplot as plt
import numpy as np
# import func

# Bild laden
img = mpimg.imread('image.jpg')

# pixels = [pixel.tolist() for row in img for pixel in row]

def blackAndWhite(pixel):
    return [0, 0, 0] if sum(pixel) < 350 else [255, 255, 255]

newImage = []
for row in img:
    newRow = []
    for pixel in row:
        newRow.append(blackAndWhite(pixel))
    newImage.append(newRow)

plt.imshow(newImage)
plt.axis('off')
plt.show()
