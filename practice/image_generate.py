import cv2
import numpy
import os

# Make an array of 120,000 random bytes
randomByteArray = bytearray(os.urandom(120000))  # We used os.urandom to generate raw bytes and convert to numpy array.
# os.urandom(120000) is equivalent to numpy.random.randint(0, 256, 120000)
flatNumpyArray = numpy.array(randomByteArray)

# Convert the array to make a 400*300 grayscale image
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('../photos/RandomGrayImage.png', grayImage)

# Convert the array to make a 400*100 color image
bgrImage = flatNumpyArray.reshape(400, 100, 3)
cv2.imwrite('../photos/RandomColorImage.png', bgrImage)

