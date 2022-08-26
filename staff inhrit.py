
class Staff:
    def codename(self):
      techer_code=int(input("Enter techer code:"))
    def codename_officer(self):
        officer_code=int(input("Enter officer code:"))
    def codename_typist(self):
        typiest_code=int(input("Enter typiest code:"))

class Teacher(Staff):
    def techinfo(self):
        techer_name=input('Enter teacher name:')
        techer_dept=input('Enter teacher department:')

tech=Teacher()
tech.codename()
tech.techinfo()

class Officer(Staff):
    def offinfo(self):
        officer_name=input('Enter officer name:')
        officer_grade=input('Enter officer grade:')
off=Officer()
off.codename_officer()
off.offinfo()

class Typist(Staff):
    def typinfo(self):
        typist_name=input('Enter typist name:')
        typist_speed=int(input('Enter typist speed:'))

typ=Typist()
typ.codename_typist()
typ.typinfo()

class Type(Typist):
    def regular(self):
        speed_typiest=(input("Enter typiest type"))

type1=Type()
type1.regular()


class Typespeed(Typist):
    def casual(self):
        speed_typiest=(input("Enter typiest type"))

type2=Typespeed()
type2.casual()



