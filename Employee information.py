from copyreg import dispatch_table


class Employee:
    def __init__(self,n,y,a):
        self.name=n
        self.year=y
        self.address=a
    #def disp(self):
    #    print( n,y,a)
       
n=[]
n=[str(item)for item in input("Enter name:").split()]
print("")
y=[]
y=[int(item)for item in input("Enter year:").split()]
print("")

a=[]
a=[str(item)for item in input("Enter address:").split()]




info=Employee(n,y,a)
#info.disp
print("Employee info")

print("name",'year','address\n',n,"\n",y,"\n",a)
