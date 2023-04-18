import numpy as np
import cv2

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('error')

dst = np.empty(src.shape, src.dtype)

print(src.shape)
print(src.shape[0])
print(src.shape[1])

for y in range(src.shape[0]):
    for x in range(src.shape[1]):
        result  = src[y,x] + 100
        if result > 255:
            result  = 255
        elif result < 0:
            result = 0
        dst[y,x] = result

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
