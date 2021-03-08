# Importing the modules
from cv2 import cv2
import numpy as np

# Declaring the canvas
img = np.ones((512,512,3),np.uint8)

# Drawing a line 
cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)

# Drawing a rectangle
cv2.rectangle(img, (50,50), (100,150), (0,0,255), cv2.FILLED)
cv2.rectangle(img, (img.shape[1]-50,img.shape[0]-50), (img.shape[1]-100,img.shape[0]-150), (0,0,255), cv2.FILLED)

# Drawing a circle
cv2.circle(img, (img.shape[1]//2,img.shape[0]//2), 50, (255,0,0), cv2.FILLED)

# Writing a text on the image
cv2.putText(img, "You are a fool", (200,200), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2)

# Displaying the canvas
cv2.imshow('Ths shapes drawn on the canvas',img)
cv2.waitKey(0)