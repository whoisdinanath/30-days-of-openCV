import cv2
import numpy

img = cv2.imread('../photos/sample.png')
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

img2 = cv2.merge((b, g, r))

cv2.imshow('hello!', img2)
cv2.waitKey(0)
