class Livro:
    def __init__(self, titulo, autor, disponivel = True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel
    def __repr__(self):
        return f"Livro('{self.titulo}', '{self.autor}')"

class Membro:
    def __init__(self, nome, livros_emprestados: list | None = None):
        self.nome = nome
        self.livros_emprestados = [] if livros_emprestados is None else livros_emprestados

    def pegar_emprestado(self, livro: Livro):
        if livro.disponivel:
            print("o livro está disponível")
            livro.disponivel = False
            print(livro.titulo)
            self.livros_emprestados.append(livro)
            print(f"'{livro.titulo}' emprestado com sucesso para {self.nome}.")
            return True
        else:
            print(f"Desculpe, '{livro}' já está emprestado.")
            return False


    def devolver_livro(self, livro: Livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponivel = True
            print(f"'{livro.titulo}' devolvido com sucesso por {self.nome}.")
            return True
        else:
            print(f"{self.nome} não possui o livro '{livro.titulo}' para devolver.")
            return False

livro1 = Livro("Dark", " Victor")
livro2 = Livro("The range", "Jake")
membro1 = Membro("Alex")
membro1.pegar_emprestado(livro1)
membro1.pegar_emprestado(livro2)
print(membro1.livros_emprestados)
membro1.devolver_livro(livro1)
print(membro1.livros_emprestados)




'''Programa simples de empréstimo de livros em uma biblioteca onde vou usar duas classes livros e membros.
Livro: tem os atributos titulo, autor, diponivel = True(de inicio)
membros: nome, livros_emprestados 
'''