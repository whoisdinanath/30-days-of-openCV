import cv2
import numpy

img = cv2.imread('../photos/sample.png')
range_of_interest = img[100:200, 100:200]
img[300:400, 300:400] = range_of_interest
cv2.imshow('hello, world!', img)
cv2.waitKey(0)
