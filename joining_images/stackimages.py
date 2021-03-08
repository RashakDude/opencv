# Importing the python modules
from cv2 import cv2
import numpy as np
from stackImages import stackImages

# Loading and converting the image in different genres
img = cv2.imread('test.jpeg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Implementing our stackImages function  
imgStack = stackImages(0.25,([img,imgGray,img],[imgGray,img,imgGray]))

# SHowing the stacked images 
cv2.imshow("ImageStack",imgStack) 
cv2.waitKey(0)