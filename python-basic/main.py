
from math_new import golden_triangle

# LAI_XUAT= 10
#
#
# a = int(input("nhập số a")) # vì nó là số nguyên nên dùng int nếu không thì kiểm tra ở dưới sẽ bị lỗi nhé
# if(a>0):
#     print("a is greater than 1");
#
#
# print(a);
#
# name = input("nhập tên của bạn: ")
# print(name + " có độ dài là " + str(len(name)))
#
# # tên biến thì nên dùng chữ thương, tên hàm thì sử dụng chữ hoa


parent_string = "I LOVE YOU"
child_string = "LOVE"

# is_found = parent_string.find(child_string)
# is_found = child_string in parent_string
# print(is_found);

# slice signature
sliced_string = parent_string[2:7]
print(sliced_string);
print(child_string[0]);
print(parent_string.upper());
print(parent_string.lower());
print(parent_string.replace("YOU", "ME"));
print(parent_string.split(" "));
print(len(parent_string));
print(parent_string.replace("YOU", "ME"));
print(parent_string.index("LOVE"));
print(parent_string.count("O"));

# format chuỗi
age= 2005
salary= 15.5
print("hiếu sinh name in year: {} và {}".format(age,parent_string));
print("hiếu sinh năm {} và lương là: {:4f}".format(age,salary));

star="*"
print(star*6)

i =1
while i<6:
    i=i+1
    if(i==3):
        continue # tiếp tục vòng lặp
    print(i)

# else với while nghĩa là nếu vừa hết while thì sẽ chạy else
print ("bắt đầu for")
for j in range(1,6):
    print(j)


for x in "hiếu võ lập trình":
    print(x)


if(golden_triangle(1,2,2)):
    print("đây là tam giác vàng")
else:
    print("đây không phải tam giác vàng")