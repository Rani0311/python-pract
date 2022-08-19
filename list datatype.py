#list datatpye
#list datatype has multiple items with different datatype.and element inside the square bracket,and seperated by comma
mylst=[1,'abc',0.2]
print(mylst)
#nested list
#in list can also have another list as an item
mylt=[1,'abc',['python',2,4],['c']]
print(mylt)
#accessimg list element
#list index-u can use index operator [] to access an item to list
#index start with 0
lst=['p','y','t','h','o','n']
print(lst[2])
print(lst[2],lst[3],lst[4])
#nested list
list1=[1,2,3,["python"],[0.4]]
print(list1[4])
#index must have integer .can not use float and other  datatype.(error in output)
list2=[1,2,3,["python"],[0.4]]
#print(list2[0.2])
#negative index-last one item has -1 then 2nd last -2 and so on
list3=[1,2,3,4,5]
print(list3[-1])
#list slicing-access the range oi item in range.strat index is inclusive but not last index exclusive
list4=[1,2,3,4,5,['python'],[1]]
print(list4[1:6])
#items beginning to end
print(list4[:])
#items from index 5 to end
print(list4[5:])
#add/ change list element
#u can use assignment operator (=).change the item and change range in item
list5=[4,3,2,1,0]
list5[0]=1
print(list5)
#change range in item(slicing)
list5[1:5]=[2,3,4,5]
print(list5)
#concataneting list using + operator
conc=[1,2,3,4]
print(conc + [5,6,7])
#repeating list using * operator
print(conc * 2)
#delete list item.using del statement
del(conc [2])
print(conc)
#delete multiple item
del(conc[0:2])
print(conc)
