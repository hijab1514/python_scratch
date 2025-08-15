"""
Encapsulation in Python
----------------------
Restrict access to variables and methods using private/protected attributes.
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

# Testing encapsulation
account = BankAccount("Fatima", 1000)
account.deposit(500)
account.withdraw(300)
print("Balance accessed via method:", account.get_balance())
# print(account.__balance)  # ❌ Error: private variable

# ---------------------------
# Practice Exercises
# ---------------------------
# 1. Create a class Student with private variable marks.
# 2. Provide methods to set and get marks.
# 3. Attempt to access the private variable directly.
