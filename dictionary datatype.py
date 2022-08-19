# dictionary datatype
a={"Rollno":1,
 "name":"abc",
 "marks":[20,10,30]
}
#print(a['ROllno'])
print(a['name'])
print(a.items)
print(a.keys)
#dictionary with integer key
my_dict={1:"abc",2:"pqr"}
print(my_dict)
#dict with mixed key
mix1={'name':"abc",1: 'pqr'}
print(mix1)
#using dict() function
mix1=dict({'roll no':1,"address": 'kagal'})
print(mix1)
#from squecnce each item as a pair
mix1=dict([(1,'xyz'),(2,'efd')])
print(mix1)

#assign element from dict
assg={'name':'apple','num':1}
#key can use [] inside 
print(assg['name'])
#or key can use get() method
print(assg.get('num'))

# change and add items in dict
#using assingement operator(=)
# existing key not change.change the value.and add another items

add1={1:'apple',2:"mango"}
#update value
add1[1]='a'
print(add1)
add1[2]="b"
print(add1)

#add items
add1[3]="c"
print(add1)

#removing items from dictionary
#using pop()method while providing key.and return value
print(add1.pop(3))
#using popitem()method while provding key and value
print(add1.popitem())
#remove all items using clear()
print(add1.clear())

#add items
add1[3]='c'
print(add1)
#delete dict
#del add1
#print(add1) #error
