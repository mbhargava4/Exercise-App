# This code is an implementation of a Pose Detector using OpenCV, Mediapipe and Math.
# The code is in the form of a class, which is called PoseDetector.
# The constructor of the class takes the following parameters: mode (default is False), upbody (default is False), smooth (default is 
# True), detectorCon (default is True), and trackingCon (default is 0.5).
# The class contains three methods.
# The first method is findPose(), which takes an image as input and returns an image with the detected landmarks. It uses Mediapipe to 
# detect the landmarks and OpenCV to draw the landmarks on the image.
# The second method is getPosition(), which takes an image as input and returns a list of the positions of each landmark. It uses OpenCV
# to draw circles around the landmarks on the image.
# The third method is getAngle(), which takes three landmarks as input and returns the angle between them. It uses Math to calculate the
# angle and OpenCV to draw lines and circles around the landmarks on the image.
# The main() function captures video from a specified file path and uses the PoseDetector class to detect and draw the landmarks and 
# angles on each frame. It displays each frame in a window and waits for the user to press the 'e' key to close the window.
# Import opencv
import cv2
# Import pathlib
import pathlib
# Import Mediapipe
import mediapipe as mp
# import Math
import math


class PoseDetector:
    # Initialize Class
    def __init__(self, mode=False, upbody=False, smooth=True,
                 detectorCon=True, trackingCon=0.5):

        self.mode = mode
        self.upBody = upbody
        self.smooth = bool(smooth)
        self.detectionCon = detectorCon
        self.trackCon = trackingCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)

    # This function helps is setting up mediapipe functions. It returns an image that refers to the video
    def findPose(self, img, draw=True):
        # Converts Image from GBR to RGB as it is what mediapipe requires as input
        imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imageRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def getPosition(self, img, draw=True):
        self.lmList = []

        if self.results.pose_landmarks:
            for node, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                x_coordinate, y_coordinate = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, x_coordinate, y_coordinate])
                if draw:
                    cv2.circle(img, (x_coordinate, y_coordinate), 5, (255, 255, 0), cv2.FILLED)
        return self.lmList

    def getAngle(self, img, p1, p2, p3, draw=True):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        angle = (180 - math.degrees(math.atan2(y3-y2, x3-x2)) + math.degrees(math.atan2(y1-y2, x1-x2)))
        angle = math.fabs(angle)
        # print(angle)


        if angle<90:
            angle = angle
        else:
            if int(angle)>270:
                angle = 360 - angle
            elif int(angle)>180 & (int(angle)<270):
                angle = 180 - angle

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (0, 0, 255), 3)
            cv2.circle(img, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), 2)
            cv2.putText(img, str(int(angle)), (x2 + 20, y2 + 20), cv2.FONT_HERSHEY_COMPLEX,
                        2, (0, 0, 255), 2)

        return angle




def main():
    p = pathlib.PureWindowsPath(r'C:\Users\manan\PycharmProjects\FinalProject459\VideoSample\pushupdemo3.mp4')
    # To capture video
    cap = cv2.VideoCapture(p.as_posix())
    poseInfo = PoseDetector()

    # To play video, we use the following for loop
    for frameIndex in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
        # Success is a boolean value that tells us whether the code can read a frame.
        # frame is a 3D array that depicts each frame in video
        success, frame = cap.read()
        img = poseInfo.findPose(frame, False)
        lmList = poseInfo.getPosition(img, False)
        poseInfo.getAngle(img, 11, 13, 15, True)
        print(lmList[12][1:])
        # cv2.circle(img, (lmList[24][1], lmList[24][2]), 5, (255, 0, 0), cv2.FILLED)
        cv2.imshow('Push Up demo', frame)

        # Checks if there is a key pressed and closes video is user pressed 'e' key
        if cv2.waitKey(10) & 0xFF == ord('e'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()