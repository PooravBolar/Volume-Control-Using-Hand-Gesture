# 🎛️ Volume Control using Hand Gestures 🎛️

This project demonstrates how to control system volume using hand gestures captured through a webcam. By utilizing computer vision, the app detects hand landmarks, calculates the distance between the thumb and index finger, and adjusts the volume accordingly. No need to touch your keyboard—just use your hands! 🖐️🔊

---

## ✨ Features:

- **Hand Gesture Detection**: Tracks hand gestures in real-time to control the system's volume.
- **Seamless Volume Control**: Adjusts the system volume by calculating the distance between your thumb and index finger.
- **Real-time Feedback**: Displays the hand and finger landmarks on the screen while the volume changes.

---

## 🧰 Requirements:

Before running the code, ensure you have the following libraries installed:

```bash
pip install cvzone
pip install numpy
pip install pycaw
pip install opencv-python

```

---

🛠️ How it Works:
Hand Detection: The app uses the cvzone and HandDetector modules to detect hands and extract landmarks.
Gesture Recognition: The distance between the thumb and index finger is calculated to determine the volume level.
Volume Adjustment: Using pycaw, the app adjusts the system volume based on the hand gesture.

---

🚀 Running the App:
Setup your Webcam: Ensure your webcam is connected.
Run the Script: Execute the Python script to start controlling the volume with your hand gestures!
```bash
python volume_control.py
```

Quit the App: Press q on your keyboard to stop the app.

---

🤝 Contribution:
Feel free to fork this project, make your modifications, and create a pull request! Any suggestions for improving the hand gesture recognition or performance are welcome.

---

📧 Contact:
Have any questions or feedback? Reach out to us at:
📩 Email: [pooravbolar3@gmail.com]

