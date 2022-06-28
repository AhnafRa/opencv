import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat_large.jpg')
cv.imshow("Pic", img)

cv.imshow('Cat',img)

def rescaleFrame(frame, scale = 0.75):


# capture = cv.VideoCapture('Videos/vid1.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
    
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()