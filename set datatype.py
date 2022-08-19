#set datatype
set1={1,2,3}
print(set1)
#set of mixed datatype
set2={1,3.2,"abc",(1,2)}
print(set2)
#set can not have mutable elements like list ,set, dictionary
#set3={1,2,3,"abd",(1,2),{2,3},[1,2]} #error occur
#print(set3)
#set can not have duplicates items
set4={1,1,2,3,3,4}
print(set4)
#we can make set from list
set4=set([ 5,6,7])
print(set4)

#cearting empty set
a={}
print(type(a)) #classtype dict

# initailze a with set() function (built in function - set)
a=set()
print(type(a)) # class set

#modifing a set using add n update
#add()-add one item in set
add1={1,3,4}
add1.add(2)
print(add1)
#update ()=add multiple items (it can takes list,tuple etc) duplicates are avoid
add1.update({4,5,6},[6,7,8])
print(add1)

#remove items from set
add1.remove(8)
print(add1)

#discard an item in set
add1.discard(7)
print(add1)

#add1.discard(9)#error
#print(add1)

#add1.remove(9) #error
#print(add1)
 #pop()
add1.pop()
print(add1)
add1.clear()
print(add1)






