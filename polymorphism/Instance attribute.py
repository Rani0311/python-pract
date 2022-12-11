#create class with instance attribute
 # write python program to create a vehicle class with max_speed & mileage instance attribute
class Vehicle:
      def __init__(self):       #instance method
            self.max_speed=80   #instance attribute
            self.mileage=20     #instance attribute
      def disp(self):
         print("vehicle max_speed  & mileage:",self.max_speed, self.mileage)     
v=Vehicle()
v.disp()