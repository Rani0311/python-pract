class Triangle:
    def perimtr(self,a,b,c):
     self.side=a
     self.side2=b
     self.side3=c
    def peri(self):
       return(self.side *self.side2* self.side3)
       #return(self.side *self.side2* self.side3/2)

       #print("perimeter of triangle:",perimter1.perimtr())

perimter1=Triangle()
perimter1.perimtr(3,4,5)
      
perimter1.peri
print("perimeter of triangle:",perimter1.peri())
#print(" semi-perimeter of triangle:",perimter1.peri())