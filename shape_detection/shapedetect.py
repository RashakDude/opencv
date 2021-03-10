# Importing the python libraries used
from cv2 import cv2
import numpy as np
from stackImages import stackImages

# Defining the function to find the contours
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for contour in contours:
        # Finding the area     
        area = cv2.contourArea(contour)
        print(area)
        # Drawing the contours
        cv2.drawContours(contourimg, contour, -1, (255,0,0), 3)
        # Finding the perimeter
        perimeter = cv2.arcLength(contour, True)
        # Finding the number of edges
        edges = cv2.approxPolyDP(contour, 0.02*perimeter, True)
        number = len(edges)
        # Shape identiification
        if number == 3 : shape = "Triangle"
        elif number == 4 : shape = "Rectangle"
        else : shape = "Circle"
        # Drawing the boundary of the shapes
        x, y, w, h = cv2.boundingRect(edges)
        cv2.rectangle(contourimg, (x,y), (x+w,y+h), (255,255,0), 3)
        cv2.putText(contourimg, shape, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)

# Loading the image
img = cv2.imread('shape.png')
contourimg = img.copy() 

# Preprocessing the image to grayscale image with Gaussian Blur effect
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 1)
canny = cv2.Canny(blur, 60, 60)
getContours(canny)

# Showing the image
stack = stackImages(0.7, ([img, gray, blur], [img, canny, contourimg]))
cv2.imshow('Images', stack)
cv2.waitKey(0)
