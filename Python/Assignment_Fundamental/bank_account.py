class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance += (self.int_rate * self.balance)
        return self
        

account = BankAccount(0.2,0)
account2 =BankAccount(0.3,57)

account.deposit(50).deposit(50).deposit(50).withdraw(90).yield_interest().display_account_info()
account2.deposit(70).deposit(500).withdraw(10).withdraw(30).withdraw(40).yield_interest().display_account_info()
#