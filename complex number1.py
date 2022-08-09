#complex number
class Complex:
    def __init__(self, r,m):
      self.real=r
      self.imaginary=m
    def add(self,o):
        return Complex(self.real+o.real,self.imaginary+o.imaginary)
comp=Complex(2,3)
comp.add(3)
print("complex number is:", comp.add())