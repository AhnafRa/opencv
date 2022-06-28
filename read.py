import cv2 as cv
from cv2 import imshow
import numpy as np

img = cv.imread('Photos/cat_large.jpg')
cv.imshow("Pic", img)

cv.imshow('Cat', img)

capture = cv.VideoCapture('Videos/vid1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
