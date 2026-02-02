class Account:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"deposited {amount}. new balance {self.balance}")
    def withdraw(self,amount):
        if(amount<=self.balance):
            self.balance-=amount
            print(f"withdrew {amount}. new balance{self.balance}")
class SavingsAccount(Account):
    MIN_balance=500
    def withdraw(self,amount):
        if self.balance-amount<self.MIN_balance:
            print("cannot withdrawal ,minimum balance should be 500")
        else:
            self.balance-=amount
            print(f"savings withdrew {amount}. new balance{self.balance}")
class CurrentAccount(Account):
    OVERDRAFT_LIMIT=-1000
    def withdraw(self,amount):
        if self.balance-amount<self.OVERDRAFT_LIMIT:
            print("you can not withdraw amount exceeding overdraft limit")
        else:
            self.balance-=amount
            print(f"withdrew{amount}. new balance{self.balance}")
def processing(acc_obj):
    acc_obj.deposit(1000)
    acc_obj.withdraw(2000)
savings=SavingsAccount(101,3000)
current=CurrentAccount(102,2000)
processing(savings)
processing(current)



    


    