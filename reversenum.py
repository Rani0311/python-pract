num=123456789
rnum=0
while num!=0:
    digit=num%10
    rnum=rnum*10+digit
    num//=10
    print('Revers number',rnum)
