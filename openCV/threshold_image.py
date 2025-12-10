import cv2
import imutils

path= r"assest/den-trang.png"
img= cv2.imread(path)

# lâấy ngưỡng
# threshold = 127 # => để đen ra đen, trắng ra trắng => ML đơn giản hơn
# max= 255
# result , threshold_result = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)


# lấy ngưỡng bằng thuật toán adaptive
threshold_result = cv2.adaptiveThreshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow("dau tay",threshold_result)

cv2.waitKey()


#  thuật toán tự động chọn ngưỡng