import cv2
import numpy
import os

randomArray = bytearray(os.urandom(720000))
numpy_array = numpy.array(randomArray)

image = numpy_array.reshape(300, 800, 3)
cv2.imwrite('../photos/fb_cover.png', image)
