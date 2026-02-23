import cv2 as cv

#img = cv.imread('Photos/cat.jpg')

#cv.imshow('Cat', img)

# Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4') # Video okuma nesnesi olusturur. 
#capture = cv.VideoCapture(0) # 0 Web kamerasini kullanir. 
while True:
    isTrue,frame = capture.read() # Video dan bir kare frame okur. 
    cv.imshow('Video', frame)

    if cv.waitKey(20) &0xFF == ord('d'): # waitKey(20) -> 20 milisaniye bekler(yani saniyede 50 kere hizinda oynatma)
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0) # Pencereyi hemen kapatmamak icin bekler. 0 parametresi bir tusa basilana kadar bekle. 
