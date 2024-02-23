class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, balance, int_rate=0): 
        # your code here! (remember, instance attributes go here)
        self.int_rate=int_rate
        self.balance=balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance+=amount
        print(f"{amount}")

        # your code here
    def withdraw(self, amount):
        if self.balance>amount:
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
        # your code here
        pass
    def display_account_info(self):
        print(f"your deposit is  {self.balance}and your {self.int_rate} ")
        
    def yield_interest(self):
        # your code here
        self.balance+=self.balance
        pass
Acc1=BankAccount(300)
Acc1.deposit(100)

Acc1.withdraw(10)
Acc1.yield_interest()

Acc1.display_account_info()
