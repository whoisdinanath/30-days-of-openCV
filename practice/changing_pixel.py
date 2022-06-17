import cv2
import numpy

# img = cv2.imread('../photos/sample.png')
# img[0, 0] = [255, 255, 255]
#
# cv2.imshow('hello, world', img)
# cv2.waitKey(0)

# changing the  value of blue at (150, 120)
img = cv2.imread('../photos/sample.png')
print(img.item(150, 120, 0))
img.itemset((150, 120, 0), 255)
cv2.imshow('hello, world!', img)
print(img.item(150, 120, 0))
cv2.waitKey(0)
