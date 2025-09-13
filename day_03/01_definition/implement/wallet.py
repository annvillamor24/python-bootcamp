"""
Class Wallet
Attribute: amount
"""

class Wallet:
    def __init__(self, amount):
        self.amount = amount

wallet = Wallet(100)
wallet.amount += 1_000_000
print(wallet.amount)