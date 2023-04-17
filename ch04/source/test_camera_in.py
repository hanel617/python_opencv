import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")

cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

while cv2.waitKey(10)<0:
    ret, frame = cap.read()
    cv2.imshow('test', frame)

cv2.destroyAllWindows()
