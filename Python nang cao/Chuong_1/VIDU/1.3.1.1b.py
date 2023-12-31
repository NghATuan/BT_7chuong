class Dog:
# Class attributes
    __DogCount = 0
    def __init__(self, name, size, age, color):
        self._name = name
        self._size = size
        self.__age = age
        self.__color = color
        Dog.__DogCount += 1

    # Getter method for _name
    def get_name(self) :
        return self._name

    # Getter method for _age
    def get_age(self) :
        return self.__age

    @classmethod
    def get_DogCount(cls) :
        return cls.__DogCount
      