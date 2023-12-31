class Dog:
# Class attributes
    DogCount = 0
    def __init__(self, name, size, age, color):
        self.name = name
        self.size = size
        self.age = age
        self.color = color

# tạo đối tượng của Lớp Dog
bull = Dog("Dom", "large", 2,"yellow" )

# in thuộc tính name của đối tượng bull
print(getattr(bull, 'name'))

# gắn giá trị của age cho 3
setattr(bull, "age", 3)

# in giá trị của age
print(getattr(bull, 'age'))

#true nếu bull chứa thuộc tính Large
print(hasattr(bull, 'large'))

# xóa thuộc tính age
delattr(bull, 'age' )

# Kích hoạt lỗi nếu age đã bị xóa
print(bull.age)