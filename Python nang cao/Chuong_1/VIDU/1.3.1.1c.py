class Dog:
    __DogCount = 0
    def __init__(self,name,size,age,color):
        self._name = name
        self._size = size
        self.__age = age
        self.color = color
        Dog.__DogCount += 1

     # Getter method for _name
    def get_name(self) :
        return self._name

    # Getter method for _age
    def get_age(self) :
        return self.__age
    
    def set_age(self,new_value):
        self.__age = new_value

obj1 = Dog("bull", "large", 2, "yellow")
obj1.set_age(5)
print("Tuổi của con chó là: {}".format(obj1.get_age()))    