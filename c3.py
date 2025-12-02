class Marks:
    def __init__(self , name , id):
        self.name = name
        self.id = id
        self.total = 0

    def total_marks(self , marks):
        self.total  = sum(marks)
        return self.total

    def percentage(self):
        return (self.total / 500) * 100

s1 = Marks("venkat",1)
print(s1.total_marks([100 , 90 , 80 , 37 , 43]))
print(s1.percentage())