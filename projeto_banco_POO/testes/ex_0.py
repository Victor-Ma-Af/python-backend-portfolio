class ContaBancaria:
    def __init__(self, titular:str):
        self.titular = titular
        self.saldo = 00
    def depositar(self, valor):
        if valor > 0:
            saldo += valor
            print(f"seu saldo atual é: {saldo}")
        else:
            print("valor a depositar deve ser maior que zero")
    def sacar(self, valor):
        if valor <= saldo and valor > 0:
            saldo -= valor
            print(f"seu saldo atual é: {saldo}")
        else:
            print("saldo insuficiente")
    def exibir_saldo(self):

        print(self.titular)
        print(self.saldo)

teste = ContaBancaria("Victor")
teste.depositar(10)