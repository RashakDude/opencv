# Importing the opencv-python module
from cv2 import cv2

# Loading the image
img = cv2.imread('test.jpeg')
print(img.shape)

# Resizing the image
img_res = cv2.resize(img, (400,600))
print(img_res.shape)

# Showing the images
cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', img_res)

# Pausing the program for infinite time
cv2.waitKey(0)