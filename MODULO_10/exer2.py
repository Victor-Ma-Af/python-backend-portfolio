'''Exercício 7 — Busca linear
Crie uma função que receba uma lista de usuários e procure um nome específico, sem utilizar .index().

Retorne a posição encontrada ou -1.'''
users = ["Ana", "João", "Ana", "Carlos", "João", "Ana"]
target = "Carlos"

def locate_target(lista: list, target):
    for user in range(len(users)):
        if users[user] == target:
            return user

    return -1

users = ["Ana", "João", "Ana", "Carlos", "João", "Ana"]
target = "Ana"

print(locate_target(users, target))