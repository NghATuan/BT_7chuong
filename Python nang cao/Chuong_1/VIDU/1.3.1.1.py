class Dog:
# Class attributes
    DogCount = 0
    def __init__(self, name, size, age, color):
        self._name = name
        self._size = size
        self.__age = age
        self.__color = color
        Dog.DogCount = Dog.DogCount + 1

obj = Dog("bull", "large", 2, "yellow")
print("Number of dogs: {}".format(Dog.DogCount))        