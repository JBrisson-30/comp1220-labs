class BankAccount:


    def __init__(self, owner, balance=0):

        self.owner = owner
        self.balance = balance


    def withdraw(self, amount):
        #check if amount is more than 0
        if amount <= 0:
            return False
        
        
        #first check if we can withdraw
        if self.balance < amount:
            #at this point we know for sure we don't have enough
            return False


        #if we can substrict and then return true
        self.balance = self.balance - amount
        return True

    def deposit(self, amount):
        if amount <= 0:
            return False
        
        self.balance = self.balance + amount
        return True

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, annual_rate=0.03):
        super().__init__(owner, balance)
        self.annual_rate = annual_rate

    def add_monthly_interest(self):
        interest = round(self.balance * self.annual_rate / 12, 2)
        self.balance = self.balance + interest
        return interest


    pass

bankAccount = BankAccount("Jonah)", 100)
was_success = bankAccount.withdraw(50)
print(was_success)
pass