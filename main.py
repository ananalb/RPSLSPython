# Brent's Bank

class Human:
    def __init__(self,):
        self.name = name
        self.email = email
        self.acct_bal = 0

    def make_deposit(self, amount):
        self.acct_bal += amount

    def make_withdrawal(self, amount):
        if self.acct_bal < amount:
            print("NSF")
        else:
            self.acct_bal -= amount

    def display_user_bal(self):
        print(f"{self.name} your current account balance is {self.acct_bal}")

    def transfer_money(self, other_user, amount):
        self.acct_bal -= amount
        other_user.acct_bal += amount

jacob = bank_account("Jacob", "jacob@gmail.com")
jacob.acct_bal = 100000
jacob.display_user_bal()

roscoe = bank_account("Roscoe", "roscoe@gmail.com")
roscoe.make_deposit(1000)

jacob.transfer_money(roscoe, 1500)
jacob.display_user_bal()
roscoe.display_user_bal()

