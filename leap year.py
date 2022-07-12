Year = int (input("Enter any Year\n"))
if(Year % 400==0 ):
    print (Year, "is leap Year")
elif (Year % 4 == 0 and Year % 100 != 0):
    print (Year, "is leap Year")

else:
    print(Year, "is not leap Year")