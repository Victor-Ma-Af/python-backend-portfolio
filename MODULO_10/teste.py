def busca_binaria_bugada(lista_ordenada, alvo):
    inicio = 0
    fim = len(lista_ordenada) -1
    cont = 0
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        cont += 1
        
        if lista_ordenada[meio] == alvo:
            return meio, f'no {cont}@ loop'
        elif lista_ordenada[meio] < alvo:
            # O alvo é maior, temos que olhar para a direita
            inicio = meio + 1
        else:
            # O alvo é menor, temos que olhar para a esquerda
            fim = meio - 1

    return -1 # Não encontrado

usuarios = [10, 25, 33, 41, 59, 68, 72, 85, 99]
print(busca_binaria_bugada(usuarios, 99))
