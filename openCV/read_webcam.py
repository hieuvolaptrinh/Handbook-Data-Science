import cv2
import numpy as np
import os

# mở webcam
camera_id=0 # là một số nguyên dương chạy từ 0-> N
cam= cv2.VideoCapture(camera_id)

# đọc ảnh liên tục từ camera => vì hiểu đơn giản video là một chuỗi ảnh liên tục
# => khung hình trên giây là fps (frame per second)
while True:
    ret, frame =cam.read()
    if(ret):
        cv2.imshow("Webcam", frame) # hiển thị ảnh từ webcam, tên là web cam, đọc hình ảnh liên tục => video

    key= cv2.waitKey(1)

    if(key ==ord('q')):
        break

cam.release() # giải phóng camera
cv2.destroyAllWindows()