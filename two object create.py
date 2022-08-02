class Student:
   def stdinfo1(self): 
    self.roll_no=1
    self. name="sam"
    self.phone_no=1234567890
    self.address="kolhapur"

   def stdinfo2(self): 
    self. roll_no=2
    self.name="john"
    self.phone_no=6565786523
    self.address="kagal"

sam_stud=Student() 
sam_stud.stdinfo1()
print("information about student1:", sam_stud.roll_no, sam_stud.name,sam_stud.address,sam_stud.phone_no)

john_stud=Student() 
john_stud.stdinfo2()
print("information about Student2:", john_stud.roll_no, john_stud.name,john_stud.address,john_stud.phone_no)
     