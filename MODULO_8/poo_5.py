'''Exercício 2 — Conta bancária
Crie uma classe ContaBancaria com titular e saldo inicial.

Implemente depositar(), sacar() e consultar_saldo().

Desafio: registre cada movimentação em uma lista historico e crie um método para exibir todas as operações realizadas.'''
class BankAccount:
    def __init__(self, owner: str, initial_balance: float):
        self.owner = owner
        self.balance = initial_balance
        self.historical = []
    def deposit(self, value):
        self.balance += value
        self.historical.append(f"deposit of {value}")
        return self.balance
    def withdrawn(self, value):
        self.balance -= value
        self.historical.append(f"withdrawal of {value}")
        return self.balance
    def check_balance():
        return self.balance

user_1 = BankAccount("victor", 100.50)
print(user_1.owner)
print(user_1.balance)

print(user_1.deposit(100))
print(user_1.deposit(100))
print(user_1.deposit(100))
print(user_1.withdrawn(50))


print(user_1.historical)
    