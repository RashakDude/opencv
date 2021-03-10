# Importing the python module
from cv2 import cv2

# Loading the image
img = cv2.imread('faces.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Importing the pre-trained cascade model provided by opencv
facecascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

# Detecting the faces 
faces = facecascade.detectMultiScale(gray, 1.1, 4)

# Drawing the faces on the image
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

# Showing the image
cv2.imshow('Resultant Image', img)
cv2.waitKey(0)
