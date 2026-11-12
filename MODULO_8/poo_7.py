'''Exercício 4 — Herança
Crie uma classe Funcionario com nome e salario.

Depois, crie duas subclasses: Desenvolvedor, com atributo linguagem, e Gerente, com atributo equipe.

Cada uma deve implementar exibir_dados() de forma diferente, utilizando super() quando apropriado.'''

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def exibir_dados(self):
         return {
            'nome' : self.nome,
            'salario' : self.salario
         }
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
            super().__init__(nome, salario)
            self.linguagem = linguagem
    def exibir_dados(self):
             return {
                'nome' : self.nome,
                'salario' : self.salario,
                'stack' : self.linguagem
            }
class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
            super().__init__(nome, salario)
            self.equipe = equipe
    def exibir_dados(self):
                 return {
                    'nome' : self.nome,
                    'salario' : self.salario,
                    'equipe' : self.equipe
                }

func_1 = Desenvolvedor('victor', 1500, 'python')
func_2 = Gerente('matin', 3000, 'equipe 5')

print(func_2.exibir_dados())
print(func_1.exibir_dados())