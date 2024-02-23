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
    def display_account_info(self):
        print(f"your deposit is  {self.balance}and your {self.int_rate} ")
        
    def yield_interest(self):
        # your code here
        self.balance+=self.balance

 


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
    	# your code here
        self.account.deposit(amount)
    
    
    def make_withdrawal(self,amount):
        self.account.withdraw(300)
    
    def display_user_balance(self):
        print(f"this{self.account.balance}")

user1=User("abdennour","a@.com")
user1.make_deposit(500)
user1.make_withdrawal(200)
print(user1.account.balance)
user1.display_user_balance()
    