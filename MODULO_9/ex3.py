# Desafio: A Função Aceita-Tudo (*args e **kwargs)
def salvar_log_avancado(acao, **kwargs):
    print(f"Ação registrada: {acao}")

    # Junta as chaves e valores formatados com vírgula e espaço, tudo em uma linha rápida
    log_formatado = ", ".join([f"{k}: {v}" for k, v in kwargs.items()])
    print(log_formatado)
    '''lista_kwargs = list(kwargs)

    for chave, valor in kwargs.items():
        if chave != lista_kwargs[-1]:
            print(f'{chave} : {valor},')
        else:
            print(f'{chave} : {valor}')
'''
salvar_log_avancado("COMPRA", valor=100.0, metodo="PIX", user_id=29 )
