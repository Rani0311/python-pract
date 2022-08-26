#inherit using construtor
class Account:
    def __init__(self) :                         # Account class construtor
        customer_name=input("Enter Name:")
        customer_acct=int(input('Enter account number:'))
        customer_acct_type=(input('Enter account type:'))
    def bal(self):
        balance=float(input("Enter amount:"))
        self.balance=balance
    def depo(self):
        deposit=float(input("Enter deposit Amount:"))
        self.balance=self.balance + deposit
        print('deposit amount is:',self.balance)

    def withd(self):
        withdrow=float(input("Enter withdrow amount:"))
        if self.balance>=withdrow:
            self.balance=self.balance - withdrow
            print('withdrow amount is:',self.balance)
        else:
            print("low balance")
    def display(self):
        if self.balance>0:
          print("Cutomer account balance",self.balance)
        else:
            print("low balance, fine ur account",self.balance)


class Curr_acct(Account):
     def __init__(self):                   #  construtor
         super().__init__()                # call  Account class construtor 
         print("you can use check book")

     
acct=Curr_acct()
acct.bal()
acct.depo()
acct.withd()
acct.display()

class Sav_acct(Account):
    def __init__(self):               # constutor
        super().__init__()            #call curr_acct class constutor
    print('You can not use check book')
    def inst(self):
     print("Interest is:")
     year=int(input('Enter year:'))
     rate=2
     interest=year * rate *self.balance
     print('Interest is',interest)

acct1=Sav_acct()
acct1.bal()
acct1.depo()
acct1.inst()
acct1.display()

