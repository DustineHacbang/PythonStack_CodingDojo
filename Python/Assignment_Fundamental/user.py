class User:
    def __init__(self, name, email_address,account_balance = 0):
        self.name = name
        self.email = email_address
        self.account_balance = account_balance

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdraw(self, amount):
        self.account_balance -= amount 
        return self   

david = User("David Stone", "david@python.com",10000)
drake = User("Drake Python", "drake@python.com")
cody = User("Cody Parker", "Cody@python.com")


david.make_deposit(150).make_deposit(150).make_deposit(150).make_withdraw(80)
drake.make_deposit(150).make_deposit(150).make_withdraw(100).make_withdraw(50)
cody.make_deposit(1500).make_withdraw(100).make_withdraw(50)

print(david.account_balance)
print(drake.account_balance)
print(cody.account_balance)


# print(david.name)	# output: Guido van Rossum
# print(cody.email)	# output: Monty Python


