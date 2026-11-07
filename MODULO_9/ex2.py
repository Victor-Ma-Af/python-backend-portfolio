# Exercício 2: Atualização de Dados (Desempacotamento)
perfil_atual = {"id": 29, "nome": "Victor", "status": "Ativo"}
dados_novos = {"status": "Inativo", "ultimo_login": "hoje"}

perfil_atualizado = {**perfil_atual, **dados_novos}
print(perfil_atualizado)