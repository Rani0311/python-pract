#list datatype methods
#append=add item end of list
app=[1,2,3,'abc']
app.append(4)
print(app)

#extend=add all element of list to another list
app.extend([5,6,7])
print(app)

#remove=remove an item for list
app.remove(7)
print(app)
#pop()=return and remove  item at the given index
app.pop(4)
print(app)
#clear()=remove all items form the list
app.clear()
print(app)
app.append(1)
print(app)
app.extend([2,3,4,5])
print(app)
#index()=returns the index .1st match item
ins=[5,2,3, 5,1]
#ins.index(3)
#print(ins)
#count()=return count of the number of item passed as an argumet
#ins.count(5)
#print(ins)
#sort()=sort item in asscending order
#ins.sort()
#print(ins)
#reverse()=reverse ALL items in list
app.reverse()
print(app)
#copy
app.copy()
print(app)

