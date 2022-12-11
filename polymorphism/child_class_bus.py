#create child class bus that will inherit all of the variables and method of vehicle class

class Vehicle:                 
    def vehicle_v(self):
        self.vehicle_type="bus"
        self.vehicle_speed="50"
    def vehicle_info(self):                #same method name
        self.vehicle_seat="35"
        
        print("  vehicle seat information:",self.vehicle_seat)
class Child_bus(Vehicle):
        def vehicle_info(self):              #same method name
             print(" child bus information")
             super().vehicle_info()           #use method overriding super()method
c=Child_bus()

c.vehicle_info()


