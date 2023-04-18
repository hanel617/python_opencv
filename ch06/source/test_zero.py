import cv2
import numpy as np

img2 = np.zeros((480,640), np.uint8)
img3 = np.ones((480,640), np.uint8) *255

cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()
