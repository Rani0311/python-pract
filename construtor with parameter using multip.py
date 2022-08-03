# construtor with parameter using multiple object
class Mobile:
    def __init__(self ,m ,v=50):
        self.model=m
        self.valume=v
    def show_info(self ,p):
        self.price=p
        print(" moblie information:" ,self.model, self.valume, self.price)
realme=Mobile( "redmi")
realme.show_info(1000)
print(id(realme))
print()

real_x=Mobile("samsung",80)
real_x.show_info(2000)
print(id(real_x))






