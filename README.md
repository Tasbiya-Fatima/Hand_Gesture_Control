# Hand_Gesture_Control
and Gesture Control using OpenCV &amp; MediaPipe
Hand Gesture Controlled System using OpenCV & MediaPipe

This project allows you to control applications and websites using hand gestures detected through a webcam. It uses OpenCV for video processing and MediaPipe Hands for accurate hand landmark detection, with added stability logic to avoid false triggers.

🚀 Features

Real-time hand detection and finger counting

Stable gesture recognition using history-based filtering

Control websites, system applications, and games

Supports both hands

Cooldown mechanism to prevent repeated triggers

Clean exit using gesture or ESC key

🛠️ Technologies Used

Python

OpenCV

MediaPipe

Webbrowser module

OS & Time modules

Deque (for gesture stability)

📌 Gesture Controls
Fingers Shown	Action Performed
1	Open Google 🌐
2	Open YouTube ▶️
3	Open WhatsApp Desktop 💬
4	Open Calculator 🧮
5	Open MS Word 📄
6	Open MS Excel 📊
7	Open Online Games 🎮
8	Open MS PowerPoint 📽️
9	Open File Explorer 📁
10	Exit Program ❌
⚙️ How It Works

Webcam captures live video feed

MediaPipe detects hand landmarks

Finger count is calculated using landmark positions

Gesture stability is verified using a deque history

Corresponding action is triggered after cooldown

Applications open based on gestures
