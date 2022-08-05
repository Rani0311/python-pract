#write program of rectangle creating two class nd enter length and breath of keyborad


class Area:
  def setDim(self):
    #self.length=l
    #self.breath=b
    self.length=int(input("Enter length:"))
    self.breadth=int(input("Enter breath:"))

  def getArea(self):

    return(self.length* self.breadth)

rect=Area()
rect.setDim()
rect.getArea()

print("area of rectangle is:",rect.getArea())