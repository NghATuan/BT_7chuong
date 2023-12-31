# class Nhan_vien:
#     id=10
#     name="Nguyen Van A"
#     age=40

#     def display (my_self):
#         print(my_self.id, my_self.name, my_self.age)

# nv1=Nhan_vien()
# nv1.display()        

class Myclass:
    def __init__(self,value):
        self.value=value

    def my_method(self):
        print('Gia tri cua doi tuong :',self.value)

#Tao mot doi tuong tu lop Myclass
obj = Myclass(50) #Khai bao va khoi tao doi tuong obj tu Myclass

#Goi phuong thuc my_method() cua doi tuong obj
obj.my_method() 

