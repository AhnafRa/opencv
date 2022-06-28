import cv2 as cv

img = cv.imread('Photos/pic.jpg')

cv.imshow('Pic', img)

# converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blurring an image
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascading
canny = cv.Canny(img, 125, 125)
cv.imshow('Cascade', canny)

# Dilating an image
dilated = cv.dilate(canny, (7, 7), iterations=1)
cv.imshow('Dilated', dilated)

# eroding an image
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# resizing an image
resized = cv.resize(img, (500, 500))
cv.imshow('Resized', resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
