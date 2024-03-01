# Import opencv
import cv2
# Import pathlib
import pathlib
# Import Mediapipe
import mediapipe as mp

# The following 2 lines of code help us replace the backslashes in a path with front slashes.
# This makes it easier for Python to locate the video file.
# This File path exists on my device.
p = pathlib.PureWindowsPath(r'C:\Users\manan\PycharmProjects\FinalProject459\VideoSample\pushupdemo3.mp4')

# To set up Pose
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils


# To capture video
cap = cv2.VideoCapture(p.as_posix())

# To play video, we use the following for loop
for frameIndex in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    # Success is a boolean value that tells us whether the code can read a frame.
    # frame is a 3D array that depicts each frame in video
    success, frame = cap.read()

    # Convert frame from GBR (which is used by OpenCV) to RGB (Which is used by Mediapipe)
    imageRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(imageRGB)

    # To draw connections between body parts
    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for node, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = imageRGB.shape
            x_coordinate, y_coordinate = int(lm.x*w), int(lm.y*h)
            cv2.circle(frame, (x_coordinate, y_coordinate), 5, (0, 255, 0), cv2.FILLED)

    # Render Video
    cv2.imshow('Push Up demo', frame)

    # Checks if there is a key pressed and closes video is user pressed 'e' key
    if cv2.waitKey(10) & 0xFF == ord('e'):
        break

# To avoid getting Error Message, we release our Video and close the windows
cap.release()
cv2.destroyAllWindows()