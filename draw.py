import cv2 as cv
import numpy as np

#This is the definition of a blank image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank Image', blank)

#A colon inside the brackets of an array means every item or pixel in the image in this case
blank[200:300, 300:400] = 255,0,0
cv.imshow('Green Image', blank)

#Draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness = 2 )
cv.imshow('R', blank)

#Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3 )
cv.imshow('Circle',blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Jason!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)