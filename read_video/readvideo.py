# Importing the opencv-python module
from cv2 import cv2

# Loading the video
cap = cv2.VideoCapture('TrumpeterSwans.mov')

# Running the video
while True:
    success, img = cap.read()
    cv2.imshow('Result', img)
    if cv2.waitKey(10) and 0xFF == ord('q'):
        break