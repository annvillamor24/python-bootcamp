class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError()

        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError()

        self._balance -= amount

    def print_balance(self):
        print(self._balance)

bank1 = BankAccount()
bank1.deposit(200)
bank1.withdraw(100)
bank1.print_balance()
