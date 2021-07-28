class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = float(file.read() or 0.0)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amout):
        self.balance += amout

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# account = Account('balance.txt')
# account.withdraw(500)
# account.deposit(1100)
# print(account.balance)
# account.commit()

class Checking(Account):
    type = 'check'

    def __init__(self, filepath, fee):
        super().__init__(filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance -= amount + self.fee


jacks_checking = Checking('jack.txt', 50)
jacks_checking.transfer(100)
jacks_checking.commit()
jacks_checking.type = 'nothing'
print(jacks_checking.type) # nothing

jhon_checking = Checking('jhon.txt', 50)
jhon_checking.transfer(100)
jhon_checking.commit()
print(jhon_checking.type) # check

