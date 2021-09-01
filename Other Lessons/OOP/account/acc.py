class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self,amount):
        self.balance=self.balance + amount
    
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """This is a class that generates checking objects"""

    type="checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee
        
checking=Checking("account\\balance.txt", 2)
print(checking.balance)
print(checking.type)
print(checking.__doc__)

jack_checking=Checking("account\\jack.txt", 2)
print(jack_checking.balance)
print(jack_checking.type)
