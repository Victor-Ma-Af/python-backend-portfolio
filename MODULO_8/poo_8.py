'''Exercício 5 — Encapsulamento
Crie uma classe Livro com título, autor e quantidade disponível.

Utilize __quantidade para representar o estoque interno. Implemente métodos para emprestar e devolver livros, validando as quantidades.

Desafio: utilize @property para permitir consultar a quantidade sem alterá-la diretamente.'''
class Livro:
    def __init__(self, titulo, autor, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_original = quantidade
        self.__quantidade = quantidade

    @property
    def quantidade(self):
        return self.__quantidade

    def devolver(self, qtd):
        if self.__quantidade < self.quantidade_original:
            self.__quantidade += qtd
            return self.__quantidade
        return 'Esse livro não é nosso'

    def emprestar(self, qtd):
        self.__quantidade -= qtd
        return self.__quantidade
# faltou estrutura codicionais para considerar coisas como qtd devolvida que faça o estoque ultrapassar valor original

l_1 = Livro('Dark', 'victor', 10)

print(l_1.emprestar(5))

print(l_1.devolver())
    