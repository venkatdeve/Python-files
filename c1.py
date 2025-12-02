#Class is blueprint
class  Person:
    def __init__(self , name , age): #special method every class should have and it is default constructor
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

p1 = Person("venkat",21) #Creating Object := instance of a class
print(p1.get_name())
print(p1.get_age())