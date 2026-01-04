def upperText(string ):
    return string.upper()

print (upperText("hello world"))

def tong(*args):
    s = 0
    for n in args:
        s += n
    return s

print(tong(1, 2))           # 3
print(tong(1, 2, 3, 4, 5)) # 15

x= lambda a,b:a+b # hàm lambda
print(x(5,6))

# hàm nhận vào chuỗi kí tư, trả ra các số trong chuỗi đó
def extract_numbers(s):
    result =""
    for c in s:
        if c.isdigit():
            result += c
    return result

print (extract_numbers("a1b2c3d4e5f6g7h8i9j0"))
# thêm global để trở thành viến toàn cục 