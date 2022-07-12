num=int(input('Enter any number'))
a=0
b=1
sum=0
if num<=0:
    print('Enter no is greater than zero\n')
else:
    for i in range(0,num):
        print(sum)
        a = b
        b = sum
        sum= a + b
