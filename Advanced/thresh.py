import cv2 as cv

img = cv.imread('Photos/pic.jpg')
cv.imshow('Pic', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded',thresh)

threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)

#Adaptive Thresholding
adaptive_thresh = cv.apdativeThreshold(gray,255, cv.APDATIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,3 )
cv.imshow('Adaptive Thresholding', adaptive_thresh)


cv.waitkey(0)