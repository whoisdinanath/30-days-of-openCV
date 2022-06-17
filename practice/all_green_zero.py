import cv2
import numpy

img = cv2.imread('../photos/sample.png')
img[:, :, 1] = 0
cv2.imshow('hello, world!', img)
cv2.waitKey(0)
