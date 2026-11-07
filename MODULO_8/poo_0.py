#Exerc 1 bank account
class BankAccount:
    def __init__(self, owner: str, initial_balance: float):
        self.owner = owner
        self.initial_balance = initial_balance
    def deposit(self, valor: float):
        self.valor = valor
        self.initial_balance += valor
        return 'your account:', self.initial_balance
    def whitdrawm(self, valor: float):
        self.valor = valor
        if self.valor <= self.initial_balance:
            self.initial_balance -= valor
            return 'your account:', self.initial_balance
        else:
            return 'your balance is insufficient'

account_1 = BankAccount("victor", 300.00)

print(account_1.deposit(100))

print(account_1.whitdrawm(150))