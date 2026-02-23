"""
Affine Dönüşüm, bir görüntünün veya koordinat sisteminin, doğrusal bir matrisle dönüştürülmesidir.
Görüntüyü döndürür, taşır, büyütür, yamultur — ama doğruları eğmez ve paralellikleri korur.

"""
import cv2 as cv
import numpy as np

img = cv.imread('Photos/istiklal.jpg')
cv.imshow('Isitiklal', img)

# Translation
def translate(img, x,y):
    transMat = np.float32([[1,0,x],[0,1,y]]) # Bu satır, dönüşüm matrisini (translation matrix) oluşturuyor.
    dimensions = (img.shape[1], img.shape[0]) # shape[1] : width genislik / shape[0] : height yükseklik
    return cv.warpAffine(img, transMat, dimensions) # affine dönüsümü uygular

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

# Rotation
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat,dimensions)

rotated = rotate(img,45)
cv.imshow('Rotated', rotated)


translate = translate(img, 100,100)
cv.imshow('Translated', translate)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img,0)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400,300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)