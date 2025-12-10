import cv2
import imutils

path= r"assest/anh-tai-project.png"
img= cv2.imread(path)


# xoay ảnh
anh_xoay= imutils.rotate(img,70)

cv2.imshow("dau tay",anh_xoay)

cv2.waitKey()