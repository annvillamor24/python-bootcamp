# class book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, amount, account):
        self.deposit(amount)

    def print_balance(self):
        print(self.balance)

account_1 = Bank(100)
BankAccount.deposit(1_000_000)