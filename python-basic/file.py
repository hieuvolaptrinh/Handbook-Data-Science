# r- đọc
# w - write
# a - append
# x - create
#
# t - text để luu trữ dạng text
# b - binary để lưu trữ dạng nhị phân thường dùng để lưu hình ảnh, video, âm thanh

# biết thôi chứ bữa sau lưu vào database
with open("demofile.txt", "rt", encoding="utf-8") as file:
    # đọc toàn bộ nội dung file vào biến contents
    contents = file.read()

print(contents)
file.close()