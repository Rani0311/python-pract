#volume of box
class Volume:
    def __init__(self,h,l,b):
        self.height=h
        self.length=l
        self.breadth=b
    def vol(self):
        return (self.height*self.length*self.breadth)      

h=int(input("Enter height:"))
l=int(input("Enter height:"))
b=int(input("Enter height:"))


v=Volume(h,l,b)
v.vol
print("volume of box is:",v.vol())
