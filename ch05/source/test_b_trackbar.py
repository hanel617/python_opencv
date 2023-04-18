import numpy as np
import cv2

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('error')

def update(pos):
    dst = cv2.add(src, pos)
    cv2.imshow('dst',dst)

cv2.namedWindow('dst')
cv2.createTrackbar('Brightness', 'dst', 0, 100, update)
update(0)

cv2.waitKey()
cv2.destroyAllWindows()
