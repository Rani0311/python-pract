#set operations
#set union= all element of both side (using= | operator )
a={1,2,3,4}
b={5,6,7,8}
print(a|b)
#use union function
print(a.union(b))
#set intersection=that are comman in both set (using & opeartor)
c={1,2,3,4,5}
d={4,5,6,7,8}
print(c & d)

# use intersection function
print(c.intersection(d))

#set diffrence=that are only in "c" not in "d"
print(c-d)
# use diffrence function
print(c.difference(d))

#symmetic diffrence=set of all item c and d but not both
print(c^d)
#use symmetric diffrence function
print(c.symmetric_difference(d))