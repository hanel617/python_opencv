import numpy as np
import cv2

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')

# dst(x,y) = src(x,y) + (src(x,y) - 128)*alpha  
alpha = 1.0
dst = np.clip(src + (src - 128.)*alpha, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

