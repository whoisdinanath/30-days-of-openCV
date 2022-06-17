import cv2

clicked = False


def on_mouse(event, x, y, flags, param):
    global clicked
    # if event == cv2.EVENT_MOUSEMOVE:
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('Hello')
cv2.setMouseCallback('Hello', on_mouse)
print('Showing Camera Feed, Press any key to cancel.')
success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('Hello', frame)
    success, frame = cameraCapture.read()
cv2.destroyWindow('Hello')
cameraCapture.release()
