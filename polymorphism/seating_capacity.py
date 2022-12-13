#create bus class that inherits from the vehicle class.give the capacity argument of bus.seating_capacity() a default value of 50
class Vehicle:
    def __init__(self):
        vehicle_type=str(input("Enter vehicle type:"))
        vehicle_speed=int(input("Enter vehicle speed:"))
        vehicle_mileage=int(input("Enter vehicle mileage:"))
class Bus(Vehicle):
    def __init__(self,bus_seating):
        self.bus_s=bus_seating
        print("Vehicle information:")
        print("bus Seat info:",self.bus_s)        
        super().__init__()                         #construtor overriding
b=Bus(50)                                         

