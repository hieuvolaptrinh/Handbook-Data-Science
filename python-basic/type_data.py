array = [1, 2, 23, 4, 4, 2, 4324]
# int, float, bool, str – số, chuỗi, đúng/sai
# list – danh sách thay đổi được
# tuple – danh sách không thay đổi được
# dict – map key → value
# set – tập hợp, không trùng phần tử, không có thứ tự
# các hàm xử lý list
print("độ dài mảng: ", len(array))
print("mảng sau khi sắp xếp: ", sorted(array))
array.append(100)
print("mảng sau khi thêm phần tử: ", array)
array.remove(2)
print("mảng sau khi xóa phần tử: ", array)
print("vị trí của phần tử 4 trong mảng: ", array.index(4))
print("số lần xuất hiện của phần tử 4 trong mảng: ", array.count(4))

# kiểu dữ liệu tuple - nó sẽ không thể thay đổi được, dùng ngoặc ()
tuple_data: tuple = (1, 2, 3, 4, 5, 6)

print("kiểu dữ liệu tuple: ", tuple_data)
# tuple_data[0]=100 # sẽ báo lỗi vì tuple không thể thay đổi được
list_converted = list(tuple_data)
list_converted.append(100)
print("tuple chuyển thành list và thêm phần tử: ", list_converted)

# kiểu dữ liệu set dúng ngoặc {}, không thể thay đổi như tuple, nhưng có thể thêm hoặc xóa phần tử, không chứa phần tử trùng lặp
tap_hop: set = {1, 2, 3, 4, 5, 5, 5, "hieus võ lập trìnhs", 5}
print("kiểu dữ liệu set: ", tap_hop)  # nó sẽ không in rac số 5 vì nó bị trùng lặp

# kiểu dữ liệu dictionary - dùng để lưu trữ dữ liệu theo kiểu key và value, dùng ngoặc {},giống như map trong các ngôn ngữ khác
# không có 2 giá trị key trùng nhau
dictionary_data: dict = {
    "123": {
        "name": "hiếu võ lập trình",
        "age": 18,
        "address": {
            "city": "hồ chí minh",
            "district": "quận 12"
        }
    },
    "456": {
        "name": "nguyễn văn a",
        "age": 20
    }
}
print("kiểu dữ liệu dictionary: ", dictionary_data)
print("lấy giá trị theo key trong dictionary: ", dictionary_data["123"]["name"])
