import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

##### We are using pycaw for the volume #####
from ctypes import cast , POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volRange = volume.GetVolumeRange()
# Min and Max volume
minVol = volRange[0]
maxVol = volRange[1]
#########################
wCam,hCam = 640,480
#########################
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False,
                        maxHands=2,
                        modelComplexity=1,
                        detectionCon=0.5,
                        minTrackCon=0.5)

# Continuously get frames from the webcam
while True:
    # Capture each frame from the webcam
    # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
    success, img = cap.read()

    # Find hands in the current frame
    # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
    # The 'flipType' parameter flips the image, making it easier for some detections
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand1 = hands[0]  # Get the first hand detected
        lmList1 = hand1["lmList"]  # (x,y,z) List of 21 landmarks for the first hand
        bbox1 = hand1["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
        center1 = hand1['center']  # Center coordinates of the first hand
        handType1 = hand1["type"]  # Type of the first hand ("Left" or "Right")

        tipOfIndexFinger = lmList1[8][0:2]
        tipOfThumbFinger = lmList1[4][0:2]
        # Calculate distance between specific landmarks on the first hand and draw it on the image
        length, info, img = detector.findDistance(tipOfIndexFinger,tipOfThumbFinger , img, color=(255, 0, 255),
                                                  scale=5)


        # Hand range 5 - 200
        # Volume range -65 - 0
        vol = np.interp(length,[20,165],[minVol,maxVol])

        volume.SetMasterVolumeLevel(vol, None)

    # Display the image in a window
    cv2.imshow("Image", img)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

