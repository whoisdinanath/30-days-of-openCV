import cv2
import numpy

img = cv2.imread('../photos/sample.png')
img[:, :, 0] = 0
cv2.imshow('Hello, world!', img)
cv2.waitKey(0)
