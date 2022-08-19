#tuple datatype
#change items
#tuple items not change .but nested mutale datatype item change(list)
chang=(1,2,3,4,["abc ",6])
chang[4][0]=5
print(chang)
#concanate the tuple
conc=(1,2,3)
print(conc + (4,5,6))
#repeat the tuple item
print(conc * 2)
#deleting the tuple.it can not delete the items in tuple
#ele=(1,2,3)
#del dele
#rint(dele)
 # tuple methods
 #index method-index of item
ins=('i','n','d','e','x')
print(ins.index('d'))
#count method-return number of time the given item is present
print(ins.count("i"))
#tuple membership -if an item exits in a tuple or not
print( "b " in ins)
print( "a " not in ins)
#itrating through a tuple
for name in('abc','pqr'):
    print("hello",name)