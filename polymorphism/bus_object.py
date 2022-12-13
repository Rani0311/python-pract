#create a bus object that will inherit all of the variable and method  of the parent vehicle class and display it
class Vehicle:
     def  __init__(self):
        vehicle_type=str(input("Enter vehicle type:"))
        vehicle_speed=int(input("Enter vehicle speed:"))
        vehicle_mileage=int(input("Enter vehicle mileage:"))
class Child(Vehicle):
      def __init__(self):
         print("vehicle Information")
         super().__init__()           #construtor overriding

bus=Child()