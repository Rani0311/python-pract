# define property have the same value for every class object
#define class attribute 'color' with the default value white.i.e every vehicle should be white
class Vehicle:
    color="white"       #class attribute
    def __init__(self):
        vehicle_type=str(input("Enter vehicle type:"))
        vehicle_speed=int(input("Enter vehicle speed:"))
        vehicle_mileage=int(input("Enter vehicle mileage:"))
class Bus(Vehicle):

    def __init__(self):
         print("Vehicle information:")
         super().__init__()     
b=Bus()
print("bus color:",Bus.color)