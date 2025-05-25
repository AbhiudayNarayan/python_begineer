# create account class with 2 attrribute - balance and acoount no
class Account :
    def __init__(self,bal ,acc ):
        self.balance = bal
        self.account = acc
    #debit method
    def debit (self,ammount):
        self.balance -= ammount
        print("ammount of rupess debited",ammount)
        print("total balance",self.balance)
    def credit (self,ammount):
        self.balance += ammount
        print("ammount of rupess credited",ammount)
        print("total balance",self.balance)
    def get_balance(self):
        return self.balance

acc1 = Account(100000 , "AFNFJ")
acc1.debit(1000)
acc1.credit(500)
acc1.credit(50000)