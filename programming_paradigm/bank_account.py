# BankAccount: This file defines the BankAccount class.
class BankAccount():
    def __init__(self, account_balance = 0.0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
# Current Balance: The account minus all the deposits and withdrawals 
    def display_balance(self):
        return self.account_balance 

   
