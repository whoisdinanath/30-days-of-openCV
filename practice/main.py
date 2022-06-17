import numpy
import cv2

img = numpy.zeros((3, 3), dtype=numpy.uint8)
print(img)

image = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print(image)

# getting the image shapes
print(image.shape)

# image = cv2.imread('../photos/sample.png', cv2.IMREAD_GRAYSCALE)
# image = cv2.imread('../photos/sample.png', cv2.IMREAD_REDUCED_GRAYSCALE_2)
image = cv2.imread('../photos/sample.png', cv2.IMREAD_REDUCED_GRAYSCALE_8)

image2 = bytearray(image)


cv2.imshow('Hello, World!', image)
cv2.waitKey(0)
# cv2.imwrite('../photos/written.jpg', image)
