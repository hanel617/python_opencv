import numpy as np
import cv2

img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('test')

cv2.createTrackbar('value', 'test', 0,255, )
