class Dog:
# Class attributes
    DogCount = 0
    def __init__(self, name, size, age, color):
        self.name = name
        self.size = size
        self.age = age
        self.color = color

    def __del__(self):
        print("A dog object is being deleted.")


obj = Dog("bull", "large", 2,"yellow" )
#del obj            