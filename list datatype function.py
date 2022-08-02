#list datatype using function
from audioop import reverse


a=[1,5,42,21,45]
a.reverse() #update list resverse
print((a))
a.append(8)# add 8 end of list
print(a)
a.sort()#update list
print(a)
a.insert(3,4) # add 4 at index 3 
print(a)
a.pop(2)#It will delete the element at index 2 and return its value
print(a)
a.remove(5) # it will remove  at the list
print(a)