class Account(object):
    def __init__(self, o, b):
        self.owner = o
        self.balance = int(b)

    def deposit(self, m):
        self.balance += m
        return self.balance

    def withdraw(self, m):
        if(m <= self.balance):
            self.balance -= m
            return self.balance
        else:
            print("Not can be overdown \nMax access: {}".format({self.balance}))
            return ""

Man = Account("Name", 50000)
print(Man.balance)
print(Man.deposit(100))
print(Man.withdraw(200))
print(Man.withdraw(100000))