import PostureDetectorModule
import cv2
import numpy as np
import pathlib
import mediapipe as mp
import math
import time

p1 = pathlib.PureWindowsPath(r'C:\Users\manan\PycharmProjects\FinalProject459\VideoSample\pushupdemo3.mp4')
cap1 = cv2.VideoCapture(p1.as_posix())
angle1arm = 0
angle1listarm = []
anglelistback = []
anglelistneck = []
dir = 0
reps = 0
ptime = time.perf_counter()
repCounted = False
detector = PostureDetectorModule.PoseDetector()

for frameIndex in range(int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))):
    success, frame = cap1.read()
    frame = detector.findPose(frame, False)
    lmlist = detector.getPosition(frame, False)

    if len(lmlist) != 0:
        detector.getAngle(frame, 11, 13, 15, False)
        anglearm = detector.getAngle(frame, 11, 13, 15, False)
        angle1listarm.append(anglearm)
        percentdone = np.interp(anglearm, (20,80), (0,100))
        ctime = time.perf_counter()
        angleback = detector.getAngle(frame, 11, 23, 25, False)
        anglelistback.append(angleback)
        angleneck = detector.getAngle(frame, 7, 11, 23, True)
        anglelistneck.append(angleneck)
        

        if percentdone==100:
            if dir==0:
                reps+=1
                dir=1
                if((ctime-ptime)<0.01):
                    reps -= 1

        if percentdone == 0:
            if dir == 1:
                dir=0


    cv2.putText(frame, str(int(reps)), (50,100), cv2.FONT_HERSHEY_COMPLEX,2,(0, 0, 255), 5)
    cv2.imshow('Push Up demo', frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap1.release()
cv2.destroyAllWindows()

max_anglearm = max(angle1listarm)
min_anglearm = min(angle1listarm)
max_angleback = max(anglelistback)
min_angleback = min(anglelistback)
max_angleneck = max(anglelistneck)
min_angleneck = min(anglelistneck)