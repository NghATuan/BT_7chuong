class Dog:
    "'Ví dụ: Minh họa các hàm thuộc tính lớp tích hợp'"
    def __init__(self, name, size, age, color):
        self.name = name
        self.size = size
        self.age = age
        self.color = color

    def display_details(self):
        print("Name:%s, size:%s, age:%d, color:%s" %
              (self.name, self.size, self.age,self.color))
bull = Dog("Dom", "large", 2, "yellow")
print("Base classes of Dog:",Dog.__bases__)
print(bull.__doc__)
print(bull.__dict__)
print(bull.__module__) 
print("Name of the class Dog:", Dog.__name__)           