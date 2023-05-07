import PostureDetectorModule
import cv2
import numpy as np
import pathlib
import mediapipe as mp
import math

p1 = pathlib.PureWindowsPath(r'C:\Users\manan\PycharmProjects\FinalProject459\VideoSample\pushupdemo3.mp4')
cap1 = cv2.VideoCapture(p1.as_posix())
angle1left = 0
angle1listleft = []
detector = PostureDetectorModule.PoseDetector()

for frameIndex in range(int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))):
    success, frame = cap1.read()
    frame = detector.findPose(frame, False)
    lmlist = detector.getPosition(frame, False)
    if frameIndex == 0:
        angle1listleft.append(0)

    if len(lmlist) != 0:
        detector.getAngle(frame, 11, 13, 15, True)
        angleleft = detector.getAngle(frame, 11, 13, 15, True)
        angle1listleft.append(angleleft)
    cv2.imshow('Push Up demo', frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap1.release()
cv2.destroyAllWindows()


max_angle1left = max(angle1listleft)
print(max_angle1left)
min_angle1left = min(angle1listleft)
print(min_angle1left)