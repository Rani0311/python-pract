class Account:
    def info(self):
        customer_name=input('Enter customer name:')
        customer_acct_no=int(input('Enter account No:'))
        account_type=input('Enter account type:')
    def bal(self):
        balance=int(input("Enter amount:"))
                
    def depo(self):
        deposit=int(input('Enter ur deposit:'))
        balance = balance + deposit
        print('add deposit and upadate balance is:',balance)
    def withd(self):
        withdrow=int(input('Enter withdrow amount:'))
        if balance>=withdrow:
           balance=balance - withdrow
        else:
            print('low balance')
        print('add withdrow and upadate balance is:',balance)

        

    




class Curr_acct(Account):
    print('you can use check book')

        

acct1=Curr_acct()
#acct1.min()
acct1.info()
acct1.bal()
acct1.depo()
#acct1.display()


class Sav_acct(Account):
     print('you do not use check book')

acct=Sav_acct()
acct.info()
acct.bal()
acct.withd()
#acct.display()
    

