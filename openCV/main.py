import  cv2
import numpy as np
import os
path= r'F:\strawbery.jpg'

img = cv2.imread(path,cv2.IMREAD_GRAYSCALE) # hàm tải ảnh từ đường dẫn
cv2.imshow('strwbery 1',img) # hiển thị ảnh với tiêu đề 'strawbery 1'

# hàm lưu ảnh imwrite, nếu ko để đường đẫn thì nó sẽ lưu thẳng vào thư mục hiện tại của file python
cv2.imwrite("assest/den-trang.png", img) # lưu ảnh vào đường dẫn mới

cv2.waitKey() # chờ 1 phím bất kì để đóng cửa sổ hình ảnh

cv2.destroyAllWindows() # đóng tất cả cửa soổ hình ảnh

# đọc từ webcam









