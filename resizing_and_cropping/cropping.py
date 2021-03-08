# Importing the opencv-python module
from cv2 import cv2

# Loading the image
img = cv2.imread('test.jpeg')

# Cropping the image
img_cropped = img[0:400,0:300]

# Showing the original and cropped image
cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', img_cropped)
cv2.waitKey(0)