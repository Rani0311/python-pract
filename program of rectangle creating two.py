#write program of rectangle creating two class nd enter length and breath of key


class Area:
  def setDim(self):
    #self.length=l
    #self.breath=b
    self.l=int(input("Enter length:"))
    self.b=int(input("Enter breath:"))

    return(self.l* self.b)
    
rect=Area()
rect.setDim
print("area of rectangle is:",rect.setDim())