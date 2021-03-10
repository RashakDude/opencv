# Importing the python modules required
from cv2 import cv2
import numpy as np

# Just an empty function 
def empty(a):
    pass

# Defining a trackbar for real time values of the thresholds
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 300)

# Setting the different values of the trackbar
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 114, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 88, 255, empty)

while True: 
    
    # Loading the image
    img = cv2.imread('test.jpeg')

    # Converting the BGR-default to HSV 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Getting the trackbar values
    h_min = cv2.getTrackbarPos("Hue MIn", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat MIn", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val MIn", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    # Setting the upper and lower limits of the mask
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Masking the image with the threshold values
    mask = cv2.inRange(hsv, lower, upper)

    # Saving the filtered out image
    result = cv2.bitwise_and(img, img, mask=mask)

    # Showing the original and hsv image
    cv2.imshow('Original Image', img)
    cv2.imshow('HSV Image', hsv)
    cv2.imshow('Masked Image', mask)
    cv2.imshow('Resulted Image', result)
    cv2.waitKey(1)