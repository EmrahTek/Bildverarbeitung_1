# Canny: Kenarlari bulur.
# Erosion: Beyaz alanlari inceltir. 
# Dilation: Beyaz alanlari genisletir. 
import cv2 as cv
import numpy as np

img = cv.imread('Photos/istiklal.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5),cv.BORDER_DEFAULT)

edges = cv.Canny(blur, 100,200)
eroded = cv.erode(edges, (3,3), iterations = 1)
dilated = cv.dilate(edges, (3,3),iterations = 1)

cv.imshow('Canny Edges', edges)
cv.imshow('Eroded', eroded)
cv.imshow('Dilated', dilated)

cv.waitKey(0)