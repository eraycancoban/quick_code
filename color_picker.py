from tkinter import Y
import cv2
from cv2 import getTrackbarPos
import numpy as np


cap = cv2.VideoCapture(0)


print("ready")


while True:

    success, img = cap.read()
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    width, height, _ =img.shape
    
    x = int(height/2)
    y = int(width/2)

    imgCenter =img_hsv[x,y]
    cv2.circle(img,(x,y),5,(0,0,255))
    print(imgCenter)

    cv2.imshow(' Color picking',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()