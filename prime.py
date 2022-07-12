num=int(input('Enter any number'))
if num>1:
    for i in range(2,num/2+1):
       if num%i==0:

        print('Enter number is  not prime',num)
    else:
        print('Enter number is  prime',num)    
else:
        print('Enter number is  not prime',num)


