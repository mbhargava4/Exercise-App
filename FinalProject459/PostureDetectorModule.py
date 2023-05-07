# Import opencv
import cv2
# Import pathlib
import pathlib
# Import Mediapipe
import mediapipe as mp


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

        # if self.results.pose_landmarks:
        #     if draw:
        #         self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
        #                                    self.mpPose.POSE_CONNECTIONS)
        return img

    def getPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for node, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                x_coordinate, y_coordinate = int(lm.x*w), int(lm.y*h)
                lmList.append([id,x_coordinate, y_coordinate])
                # if draw:
                #     cv2.circle(img, (x_coordinate, y_coordinate), 5, (0, 255, 0), cv2.FILLED)
        return lmList


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
        img = poseInfo.findPose(frame, True)
        lmList = poseInfo.getPosition(img, True)
        print(lmList[24])
        cv2.circle(img, (lmList[24][1], lmList[24][2]), 5, (255, 0, 0), cv2.FILLED)
        cv2.imshow('Push Up demo', frame)

        # Checks if there is a key pressed and closes video is user pressed 'e' key
        if cv2.waitKey(10) & 0xFF == ord('e'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()