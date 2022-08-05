# find area and perimeter of trangle using construtor
class Triangle:
    def __init__ (self,a,b,c):
        self.side1=a
        self.side2=b
        self.side3=c
    def perimtr(self):
        return(self.side1*self.side2*self.side3)
    
    
angle=Triangle(3,4,5)
angle.perimtr
print("perimeter of triangle:",angle.perimtr())