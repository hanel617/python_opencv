import numpy as np
import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

w = 640
h = 480

#w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)


print(w)
print(h)
print(fps)


fourcc = cv2.VideoWriter_fourcc(*'DIVX')
delay = round(1000 / fps)

outputVideo = cv2.VideoWriter('output.avi', fourcc, 20.0, (w, h))
if not outputVideo.isOpened():
    print('File open failed!')



while True:
    ret, frame = cap.read()
    outputVideo.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(delay) == 27:
        break

cv2.destroyAllWindows()
