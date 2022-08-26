# multiple ineritance
class Teacher:
    def techinfo(self):
        techer_name=input('Enter teacher name:')
        techer_dept=input('Enter teacher department:')
        techer_exp=int(input('Enter teacher Exprince:'))



class Officer:
    def offinfo(self):
        officer_name=input('Enter officer name:')
        officer_grade=input('Enter officer grade:')
        officer_exp=int(input('Enter officer Exprince:'))

class Eduction(Teacher,Officer):     #two class inherit 

    def edu_info(self):
        print('Eduction information')
        high=input('Highest qualification:')
        high_p=input('highest professional qualification: ')

educt=Eduction()
educt.techinfo()
educt.edu_info()
educt.offinfo()
educt.edu_info()
