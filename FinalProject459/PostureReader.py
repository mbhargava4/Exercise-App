# Import opencv
import cv2 
# Import pathlib
import pathlib 

# The following 2 lines of code help us replace the backslashes in a path with front slashes.
# This makes it easier for Python to locate the video file.
# This File path exists on my device.
p = pathlib.PureWindowsPath(r'C:\Users\manan\PycharmProjects\FinalProject459\VideoSample\pushupdemo2.mp4')
print(p.as_posix())

# To capture video 
cap = cv2.VideoCapture(p.as_posix())

# To print duration of video (Frame Count/ Frames Per Second)
print(cap.get(cv2.CAP_PROP_FRAME_COUNT)/cap.get(cv2.CAP_PROP_FPS))

# To play video, we use the following for loop
for frameIndex in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    # Success is a boolean value that tells us whether the code can read a frame.
    # frame is a 3D array that depicts each frame in video
    success, frame = cap.read() 
    
    # Render Video
    cv2.imshow('Push Up demo', frame)
    
    #
    if cv2.waitKey(10) & 0xFF == ord('e'):
        break

# To avoid getting Error Message, we release our Video and close the windows
cap.release()
cv2.destroyAllWindows()