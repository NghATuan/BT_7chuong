class Dog:
    #Constructor không tham số
    def __init__(self):
        print('Đây là constructor không tham số')

    def display(self, name):
        print('Hello',name)

bull = Dog()
bull.display("The Dom")
            