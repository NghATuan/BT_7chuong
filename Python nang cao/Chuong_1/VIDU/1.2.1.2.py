class Dog:

    DogCount = 0       #Thuộc tính của lớp
    #hàm khởi tạo đối tượng
    def __init__(self, name, size, age, color):
        self.name = name
        self.size = size
        self.age = age
        self.color = color

    def Go(self):
        print("I'm going...")
    def Stay(self, place):
        print("I'm staying at {}".format(place))
    def Lie(self, place):
        print("I'm lying at {}".format(place))
    def Bank(self):
        print("Whoop...")
    def Eat(self, food):
        print("I'm eating {}".format(food))

# Khởi tạo đối tượng
bull = Dog("Bull", "large", 2, "Yellow");
bull.Eat("bone")
bull.Go("PARTY")
bull.Bank()                    
