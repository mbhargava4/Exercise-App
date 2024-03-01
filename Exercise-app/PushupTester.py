# This code reads in a video file of a person doing push ups and uses the PoseDetector class from the PostureDetectorModule to detect the 
# angles of the arms, back, and neck of the person in each frame of the video. It then checks if the push up is being performed correctly 
# by checking if the angle of the back and neck are within certain ranges defined in the pushuplearner module. If the back or neck angles 
# are outside of those ranges, it will display a message on the video indicating that the user is performing the push up incorrectly. It 
# also keeps track of the number of push ups performed correctly and displays it on the video. The code terminates when the user presses 
# the 'e' key.
import pushuplearner as pl
import PostureDetectorModule
import cv2
import numpy as np
import pathlib
import mediapipe as mp
import time

p1 = pathlib.PureWindowsPath(r'C:\Users\manan\PycharmProjects\FinalProject459\VideoSample\pushupdemo4.mp4')
cap1 = cv2.VideoCapture(p1.as_posix())
dir = 0
reps = 0
repCounted = False
neckstrain = False
badback = False
detector = PostureDetectorModule.PoseDetector()

for frameIndex in range(int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))):
    success, frame = cap1.read()
    frame = detector.findPose(frame, False)
    lmlist = detector.getPosition(frame, False)

    if len(lmlist) != 0:
        detector.getAngle(frame, 11, 13, 15, False)
        anglearm = detector.getAngle(frame, 11, 13, 15, False)
        percentdone = np.interp(anglearm, (20,80), (0,100))
        ctime = time.perf_counter()
        angleback = detector.getAngle(frame, 11, 23, 25, False)
        angleneck = detector.getAngle(frame, 7, 11, 23, False)

        if percentdone==100:
            if dir==0:
                reps+=1
                dir=1


        if percentdone == 0:
            if dir == 1:
                dir=0


        if angleback>pl.max_angleback+10 or angleback<pl.min_angleback:
            cv2.putText(frame, "Back is not straight", (25, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
            badback= True
            ctime1 = time.perf_counter()
            angleback = detector.getAngle(frame, 11, 23, 25, True)
            if reps>0:
                reps -= 1
            else:
                reps = 0


        if angleneck>pl.max_angleneck+5 or angleneck<pl.min_angleneck:
            cv2.putText(frame, "That will put too much strain on your Neck", (30, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
            neckstrain = True
            ctime2 = time.perf_counter()
            angleback = detector.getAngle(frame, 11, 23, 25, True)
            if reps>0:
                reps -= 1
            else:
                reps = 0

    cv2.imshow('Push Up demo', frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap1.release()
cv2.destroyAllWindows()