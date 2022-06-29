import cv2 as cv
import numpy as np

img = cv.imread('Photos/pic.jpg')
cv.imshow('Pic',img)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Blank', blank)

gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blur = cv.GaussianBlur, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

contours, hiearchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} countours were found')

cv.waitKey(0)