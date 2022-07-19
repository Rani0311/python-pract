from pickle import APPEND
from posixpath import split

num1= list(map (int(input("Enter numbers")).split()))
if num1/5:
    for num1 in range(num1<=150 ):
        print(num1)
        if num1 >150 and num1<500:
           for num1 in range(num1<=500):
            print(num1)
else:
    print("number is not divided by 5", num1)
