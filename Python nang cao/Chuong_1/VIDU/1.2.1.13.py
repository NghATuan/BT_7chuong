class Dog:
# Class attributes    
    DogCount = 0
    def __init__(self, name, size, age, color):
        self.name = name
        self.size = size
        self.age = age
        self.color = color
        Dog.DogCount = Dog.DogCount + 1
    
    def __def__(self):
        print("A dog object is being deleted.")
        Dog.DogCount=Dog.DogCount - 1

obj1 = Dog("bull", "large", 2, "yellow")
obj2 = Dog ("Poodle", "small", 1, "white")
print ("Number of dogs: {}".format(Dog.DogCount))        

    