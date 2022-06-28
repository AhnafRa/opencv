import cv2 as cv

img = cv.imread('Photos/pic.jpg')
cv.imshow('Pic',img)

gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

contours, hiearchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} countours were found')

cv.waitKey(0)