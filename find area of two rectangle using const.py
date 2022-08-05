# find  area of two rectangle using construtor with parameter
class Rectangle:
    def __init__(self, l,b):
        self.length=l
        self.breath=b
    def area(self):
        return(self.length*self.breath)


rect1=Rectangle( 4,5)
rect1.area
print("Area of rectangle:",rect1.area())
print()

rect2=Rectangle(5,8)
rect2.area
print("Area of rectangle:",rect2.area())

