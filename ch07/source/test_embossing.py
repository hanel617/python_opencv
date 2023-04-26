import numpy as np
import cv2

img = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

#chatGPT example
kernel = np.array([[-2,-1,0],[-1,1,1],[0,1,2]])
emboss = cv2.filter2D(img,-1, kernel)

#book simple example
kernel2 = np.array([[-1,-1,0],[-1,0,1],[0,1,1]])
emboss2 = cv2.filter2D(img,-1, kernel2)

#book example
emboss3 = cv2.filter2D(img,-1, kernel2,delta=128 )

#test
kernel4 = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
emboss4 = cv2.filter2D(img,-1, kernel4,delta=128 )

kernel5 = np.array([[1,0,0],[0,0,0],[0,0,-1]])
emboss5 = cv2.filter2D(img,-1, kernel5,delta=128 )

kernel6 = np.array([[0,0,-1],[0,0,0],[-1,0,1]])
emboss6 = cv2.filter2D(img,-1, kernel6,delta=128 )

cv2.imshow('img',img)
cv2.imshow('emboss',emboss)
cv2.imshow('emboss2',emboss2)
cv2.imshow('emboss3',emboss3)
cv2.imshow('emboss4',emboss4)
cv2.imshow('emboss5',emboss5)
cv2.imshow('emboss6',emboss6)


cv2.waitKey(0)
cv2.destroyAllWindows()
