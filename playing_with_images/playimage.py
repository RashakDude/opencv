# Importing the opencv-python module
from cv2 import cv2
import numpy as np

# Loading the image to be used 
img = cv2.imread('test.jpeg')

# Converting the image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('GrayScale Image', gray)

# Blurring the grayscale image
blur = cv2.GaussianBlur(gray, (7,7), 0)
cv2.imshow('Blurred Image', blur)

# Edge detection 
edges = cv2.Canny(img, 100, 100)
cv2.imshow('Canny Image', edges)

# Increase the thisckness of the edges so that the lines can be joined well
kernel = np.ones((3,3),np.uint8)
dialation = cv2.dilate(edges, kernel, iterations=1)
cv2.imshow('Dilated Image', dialation)

# Waiting the process for the infinite time
cv2.waitKey(0)