from operator import countOf


#msg analyzer program
a=(input("Enter msg \n"))
print(len(a))

if "e" in a:
    print( " is in msg")
else:
    print("is not in msg")