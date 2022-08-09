class Complex:
    def __init__ (self,r,o):
        self.real=r
        self.imaginary=o
    def comp(self):
        return complex(r+o) 
r=int(input("Enter real number:"))
o=int(input("Enter imaginary number:"))        
complex_no=Complex(r,o)
complex_no.comp()
print("complex number is:",complex_no.comp())
