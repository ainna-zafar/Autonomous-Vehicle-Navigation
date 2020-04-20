import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('smarties.jpg', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 225, cv2.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=1)
opening= cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
closing= cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', closing]
images=   [img, mask, dilation, erosion, opening, closing]
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()





