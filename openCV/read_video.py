import cv2
import numpy as np
import os

video_file = r'assest/introl_tikTok_final.mp4'
cam = cv2.VideoCapture(video_file)

# Tạo window cho phép resize
cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Webcam", 800, 600)  # kích thước ban đầu

while True:
    ret, frame = cam.read()
    if not ret:
        break  # hết video thì thoát

    # Nếu muốn thu nhỏ frame thật sự (không chỉ cửa sổ), có thể:
    # frame = cv2.resize(frame, (800, 600))

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
