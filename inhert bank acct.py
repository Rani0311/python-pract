class Account:
    def info(self):
        customer_name=input('Enter customer name:')
        customer_acct_no=int(input('Enter account No:'))
        account_type=input('Enter account type:')
    def bal(self):
        self.balance=12345
                
    def depo(self):
        deposit=int(input('Enter ur deposit:'))
        self.balance = self.balance + deposit
        print('add deposit and upadate balance is:',self.balance)
    def withd(self):
        withdrow=int(input('Enter withdrow amount:'))
        if self.balance>=withdrow:
           self.balance=self.balance - withdrow
        else:
            print('low balance')
        print('add withdrow and upadate balance is:',self.balance)

        

    




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
    

