
# **
# Inheritance - kế thừa
# Polymorphism - đa hình
# Encapsulation - đóng gói
# Abstraction - trừu tượng
# *#


class IdoGioiTre:
    # ecapsulation
    def __init__(self,name,age, appearance):
        self.name = name
        self.age = age
        self.__appearance = appearance  #set private variable

    def __str__(self):
        return f"Tên: {self.name}, Tuổi: {self.age}, Ngoại hình: {self.__appearance}"

    def setAppearance(self, appearance):
        self.__appearance = appearance

class KhaBanh(IdoGioiTre):

    def __init__(self, name, age, appearance,location):
        super().__init__(name, age, appearance)
        self.location = location

    def liveStream(self):
        pass

    def signatureQuote(self):
        print("Đời là bể khổ, ta phải cố gắng lên!")


khaBanh= KhaBanh("Kha Banh", 22, "handsome","trong tù")
khaBanh.setAppearance("tóc như LL")
print(khaBanh)