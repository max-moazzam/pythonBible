#Bank

class Account:
    def __init__(self, name, balance, minBalance):
        self.name = name
        self.balance = balance
        self.minBalance = minBalance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= self.minBalance:
            self.balance -= amount
        else:
            print("You have insufficent funds!")

    def statement(self):
        print("Account Balance: ${}".format(self.balance))

class CurrentAccount(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, minBalance = -1000)

    def __str__(self):
        return "{}'s Current Account : Balance: ${}".format(self.name, self.balance)

class SavingsAccount(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, minBalance = 0)

    def __str__(self):
        return "{}'s Savings Account : Balance: ${}".format(self.name, self.balance)
