import cv2

cameraCapt = cv2.VideoCapture(0)
fps = 30
size = (int(cameraCapt.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cameraCapt.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('../videos/camera_capt.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
success, frame = cameraCapt.read()
frames_remaining = 10 * fps - 1
while success and frames_remaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapt.read()
    frames_remaining -= 1
cameraCapt.release()
