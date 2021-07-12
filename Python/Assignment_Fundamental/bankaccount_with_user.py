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


class User:

    account=[]

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount (int_rate=0.44,balance=550)

    def deposit(self):
        self.account.deposite()
        print(self.account.balance)





david = User("David Stone", "david@python.com")
cody = User("Cody Parker", "Cody@python.com")

david.account.deposit(150).deposit(150).deposit(150).withdraw(80).display_account_info()
cody.account.deposit(1500).withdraw(100).withdraw(50).display_account_info()
