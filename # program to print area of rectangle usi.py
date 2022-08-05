# program to print area of rectangle  using construtor with parameter.and Enter length and breath of rectangle from user
class Area:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def return_area(self):
        return(self.length*self.breadth)
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))

rect=Area(l,b)
rect.return_area()
print("area of rectangle is:",rect.return_area())