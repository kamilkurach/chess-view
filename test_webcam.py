'''Test webcam output.'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cap = cv.VideoCapture(-1)

while(True):

    ret, frame = cap.read()

    if ret == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        edges = cv.Canny(gray,50,150,apertureSize = 3)

        cv.imshow('OpenCV output', frame)
        # cv.imshow('OpenCV output', gray)
        # cv.imshow('OpenCV output', edges)
        # print(cv.getWindowImageRect('OpenCV output'))
  
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()
