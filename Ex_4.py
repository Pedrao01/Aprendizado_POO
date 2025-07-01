class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self._banc = 'Bradesco'
        self.__balance = balance

    def show_balance(self):
        print(f'Show balance: {self.__balance}')

accont1 = Account('Pedro', 900000)
print(accont1.owner)
print(accont1._banc)
accont1.show_balance()
accont1.__balance = 2
accont1.show_balance()
print(accont1.__balance)
print(accont1._Account__balance)