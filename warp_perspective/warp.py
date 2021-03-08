# Importing the python modules
from cv2 import cv2
import numpy as np

# Loading the image 
img = cv2.imread("cards.jpg")

# Specifying the height and width of the card 
width,height = 250,350

# Spedcifying the area of the card to be mapped with another area
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# Perpective Transformation and wrapping
matrix = cv2.getPerspectiveTransform(pts1,pts2)
warp = cv2.warpPerspective(img,matrix,(width,height))

# Displaying the result 
cv2.imshow("Original Image",img)
cv2.imshow("Warped Image",warp)
cv2.waitKey(0)