import random
from senha.constantes import ListaCarac, ListaNum


def geraSenha():
    caracteres = random.choices(ListaCarac, k=6)
    nums = random.choices(ListaNum, k=2)
    return "".join(caracteres) + "".join(str(n) for n in nums)
