# Importing the opencv-python module
from cv2 import cv2

# Reading the image
img = cv2.imread('test.jpeg')

# Showing the image
cv2.imshow('Result', img)
cv2.waitKey(0)