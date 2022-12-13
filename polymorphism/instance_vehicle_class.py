#determine if school_bus is also an instance of the vehicle class
class Vehicle:
    def v_info(self):
        v_type=str(input("Enter vehicle type:"))
        v_speed=int(input("Enter vehicle speed:"))
        v_mileage=int(input("Enter vehicle mileage:"))

class Bus(Vehicle):
    def bus_info(self,seat):
        v_seat=int(input("Enter Seat:"))
    
school_bus=Bus()
print(isinstance(school_bus,Vehicle))   # use isinstance(object,classname) function




        


