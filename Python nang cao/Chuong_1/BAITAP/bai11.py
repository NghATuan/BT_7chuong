class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class TamGiacVuong(TamGiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)  # Gọi hàm khởi tạo của lớp cha
        # Kiểm tra xem có phải tam giác vuông không
        if self.a ** 2 + self.b ** 2 == self.c ** 2 or self.a ** 2 + self.c ** 2 == self.b ** 2 or self.b ** 2 + self.c ** 2 == self.a ** 2:
            print("Đây là tam giác vuông.")
        else:
            print("Đây không phải là tam giác vuông.")

class TamGiacCan(TamGiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)  
        if self.a == self.b or self.a == self.c or self.b == self.c:
            print("Đây là tam giác cân.")
        else:
            print("Đây không phải là tam giác cân.")

class TamGiacDeu(TamGiacCan):
    def __init__(self, a, b, c):
        super().__init__(a, b, c) 
        if self.a == self.b == self.c:
            print("Đây là tam giác đều.")
        else:
            print("Đây không phải là tam giác đều.")

tam_giac = TamGiac(3, 4, 5)
tam_giac_vuong = TamGiacVuong(3, 4, 5)
tam_giac_can = TamGiacCan(3, 3, 4)
tam_giac_deu = TamGiacDeu(3, 3, 3)  
