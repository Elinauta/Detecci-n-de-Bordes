import cv2
from cv2 import Sobel
import numpy as np

video = cv2.VideoCapture(0)

while True:
    ret,frame = video.read()
    if ret==True:
        frame_hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        laplaciano = cv2.Laplacian(frame, cv2.CV_64F)
        sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
        sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
        #cv2.Canny(imagen, umbral min, umbral max)
        bordes = cv2.Canny(frame,100,250)

        cv2.imshow('Frame', frame)
        
        cv2.imshow('Laplaciano', laplaciano)
        cv2.imshow('Sobel X', sobelx)
        cv2.imshow('Sobel Y', sobely)
        cv2.imshow('Canny sin  filtrar', bordes)

        if cv2.waitKey(1) & 0xFF== ord('s'):
            break

video.release()        
cv2.destroyAllWindows()