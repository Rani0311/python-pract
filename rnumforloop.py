num = input("Enter 10  number")
rnum = ''
for i in range(len(num),0,-1):
   # i = num % 10
    rnum =num[i-1]
   # num //= 10
    print('Reverse number',rnum)
