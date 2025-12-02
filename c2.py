
class Bank:
    acc_number = 1010124
    def __init__(self , name):
        self.name = name
        self.acc_number = Bank.acc_number
        Bank.acc_number += 1
        selfe = 0

    def withdraw(self , amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("INSUFFICIENT  BALANCE")

    def deposit(self , amount):
        self.balance += amount

    def check_balance(self ):
        return self.balance

    def account_number(self):
        return self.acc_number


b1 = Bank("venkat") # default constructor Object Create
b1.deposit(1000)
print(b1.check_balance())
b1.withdraw(500)
print(b1.check_balance())
b1.withdraw(1000)
print(b1.acc_number)

b2 = Bank("Varma")
print(b2.account_number())

