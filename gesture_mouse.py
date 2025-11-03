import cv2
import mediapipe as mp
import pyautogui
import math
import numpy as np
import time

# Initialize MediaPipe and PyAutoGUI
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,       # fewer hands = faster
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
                       )
screen_w, screen_h = pyautogui.size()

# Capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height


# Smoothing variables1
prev_x, prev_y = 0, 0
smooth_factor = 5  # smaller = faster response, larger = smoother

last_click_time = 0
click_cooldown = 0.3

frame_count = 0

try:
    while True:
        ret, frame = cap.read()
        frame_count += 1
        if frame_count % 2 != 0:
            continue

        if not ret:
            break

        # Flip and reduce frame size for speed
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extract landmarks
                index_finger_tip = hand_landmarks.landmark[8]
                thumb_tip = hand_landmarks.landmark[4]
                middle_tip = hand_landmarks.landmark[12]

                ix, iy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
                tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)
                mx, my = int(middle_tip.x * w), int(middle_tip.y * h)

                # Draw markers
                cv2.circle(frame, (ix, iy), 6, (0, 255, 0), -1)
                cv2.circle(frame, (tx, ty), 6, (255, 0, 0), -1)

                # Convert to screen coordinates
                screen_x = np.interp(ix, [0, w], [0, screen_w])
                screen_y = np.interp(iy, [0, h], [0, screen_h])

                # Apply smoothing
                curr_x = prev_x + (screen_x - prev_x) / smooth_factor
                curr_y = prev_y + (screen_y - prev_y) / smooth_factor
                pyautogui.moveTo(curr_x, curr_y)
                prev_x, prev_y = curr_x, curr_y

                # Measure distances
                thumb_index_dist = math.hypot(tx - ix, ty - iy)
                index_middle_dist = math.hypot(ix - mx, iy - my)

                # Click gesture
                if thumb_index_dist < 25:
                    now = time.time()
                    if now - last_click_time < 0.5:
                        pyautogui.doubleClick()
                        cv2.putText(frame, "Double Click", (30, 80),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                    else:
                        pyautogui.click()
                        cv2.putText(frame, "Click", (30, 80),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                    last_click_time = now
                    time.sleep(click_cooldown)

                # Drag gesture
                elif 25 < thumb_index_dist < 40:
                    pyautogui.mouseDown()
                    cv2.putText(frame, "Dragging", (30, 120),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 100, 0), 2)
                else:
                    pyautogui.mouseUp()

                # Scroll gesture (index + middle)
                if index_middle_dist < 35:
                    if my < iy:
                        pyautogui.scroll(100)
                        cv2.putText(frame, "Scroll Up", (30, 160),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    else:
                        pyautogui.scroll(-100)
                        cv2.putText(frame, "Scroll Down", (30, 160),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Gesture Mouse [Optimized]", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
except KeyboardInterrupt as e:
    cap.release()
    cv2.destroyAllWindows()
    print(e)

cap.release()
cv2.destroyAllWindows()
