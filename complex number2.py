import math
class Complex:

    def __init__ (self,r,o):
        self.real=r
        self.imaginary=o
    def comp(self):
        return complex(r+o) 
    def sum(self):
        return Complex(self.real+self.imaginary)
lit=[]
r=list(input("Enter real number:"))
o=list(input("Enter imaginary number:"))        
complex_no= Complex(r,o)
complex_no.comp
complex_no.sum()
print("complex number is:",complex_no.comp())
print("complex number is:",complex_no.sum())
