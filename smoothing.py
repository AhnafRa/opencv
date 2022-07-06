import cv2 as cv

img = cv.imread('Photos /pic.jpg')
cv.imshow('Pic',img)

#Average method for blurring
avg = cv.blur(img, (3,3))
cv.imshow('Average', avg)

#Gaussian Blur method
gaus = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian', gaus)

#Median Blur method
med = cv.medianBlur(img,3)
cv.imshow('Median', med)

#Bilateral Blurring
bilat = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilat)

cv.waitKey(0)