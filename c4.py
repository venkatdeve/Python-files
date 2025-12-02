class Duck:
    def quack(self):
        print("Quack Quack")
class Person():
    def quack(self):
        print("Iam duck")
def make_it_quack(obj):
    obj.quack()

make_it_quack(Person())
make_it_quack(Duck())


#Inhertiance
class A:
    def show(self):
        print("A class")
class B:
    def show(self):
        print("B class")

class C(B,A):
    pass

obj = C()
obj1 = B()
obj1.show()
obj.show()
