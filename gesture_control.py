import cv2
import mediapipe as mp
import webbrowser
import os
import time
from collections import deque

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)
mp_draw = mp.solutions.drawing_utils

# Finger tip indices (Mediapipe landmarks)
finger_tips = [8, 12, 16, 20]
thumb_tip = 4

# Video capture
cap = cv2.VideoCapture(0)

# Stability settings
finger_history = deque(maxlen=15)  # Increase history for more stability
last_triggered = None
last_action_time = 0
cooldown = 2  # seconds

def count_fingers(hand_landmarks, hand_label):
    """Count fingers with better thresholds for stability."""
    lm = hand_landmarks.landmark
    fingers = 0

    # Thumb logic
    if hand_label == "Right":
        if lm[thumb_tip].x < lm[thumb_tip - 1].x - 0.02:
            fingers += 1
    else:
        if lm[thumb_tip].x > lm[thumb_tip - 1].x + 0.02:
            fingers += 1

    # Other fingers
    for tip in finger_tips:
        if lm[tip].y < lm[tip - 2].y - 0.03:
            fingers += 1

    return fingers

def trigger_action(fingers):
    """Perform action based on stable finger count."""
    global last_triggered, last_action_time

    now = time.time()

    # Avoid repeated triggers
    if fingers == last_triggered or now - last_action_time < cooldown:
        return

    try:
        if fingers == 1:
            webbrowser.open("https://www.google.com")
        elif fingers == 2:
            webbrowser.open("https://www.youtube.com")
        elif fingers == 3:
            os.system("start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
        elif fingers == 4:
            os.system("calc")
        elif fingers == 5:
            os.system("start winword")
        elif fingers == 6:
            os.system("start excel")
        elif fingers == 7:
            games = [         
                "https://www.gamesgames.com/"             
            ]
            for game_url in games:
                webbrowser.open(game_url)
        elif fingers == 8:
            os.system("start powerpnt")
        elif fingers == 9:
            os.system("explorer")
        elif fingers == 10:
            cap.release()
            cv2.destroyAllWindows()
            exit()
    except Exception as e:
        print(f"Action failed: {e}")

    last_triggered = fingers
    last_action_time = now


while True:
    success, frame = cap.read()
    if not success:
        print("Camera not found or cannot read frame.")
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    total_fingers = 0

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, hand_info in zip(
            results.multi_hand_landmarks, results.multi_handedness
        ):
            hand_label = hand_info.classification[0].label
            total_fingers += count_fingers(hand_landmarks, hand_label)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        finger_history.append(total_fingers)

        # Stability check: at least 70% of recent frames must match
        if finger_history.count(total_fingers) >= int(0.7 * finger_history.maxlen):
            trigger_action(total_fingers)

    cv2.putText(
        frame,
        f"Stable Fingers: {total_fingers}",
        (30, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 255, 0),
        3
    )

    cv2.imshow("Hand Gesture Control (Stable)", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
