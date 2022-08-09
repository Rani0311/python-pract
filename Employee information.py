from copyreg import dispatch_table


class Employee:
    def __init__(self,n,y,a):
        self.name=n
        self.year=y
        self.address=a
    def disp(self):
        print( n,y,a)
       
lst=[]
n=str(input("Enter name"))
list=n.split()
y=int(input("Enter year"))

a=str(input("Enter adress"))
list=a.split()


info=Employee(n,y,a)
info.disp
print("Employee info")

print("name",'year','address\n',n,y,a)
