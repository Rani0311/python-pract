#multi-level inhertance

class Master:
    def __init__(self):
        print("information of account and admin")
class Acct(Master):
    def pay(self):
        account_code=int(input('Enter Account code:'))
        payment=int(input('Enter amount:'))
        self.payment=payment
class Admin (Acct):
    def exp(self):
        admin_code=int(input('Enter admin code:'))
        exprince=input("Enter exprince:")
        self.exprince=exprince

class Person(Admin):
    def display(self):
      print('information')

    

per=Person()
per.display()
per.exp()
per.pay()



