import cv2

video = cv2.VideoCapture('../videos/sample.avi')
fps = video.get(cv2.CAP_PROP_FPS)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# videoWriter = cv2.VideoWriter('../videos/written2.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
videoWriter = cv2.VideoWriter('../videos/written.avi', cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size)
success, frame = video.read()
while success:
    videoWriter.write(frame)
    success, frame = video.read()
