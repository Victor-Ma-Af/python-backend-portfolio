# Exercício 1: O Filtro Elegante (List Comprehension)
processos = [
    {"pid": 1, "nome": "Chrome", "memoria": 400},
    {"pid": 2, "nome": "VS Code", "memoria": 800},
    {"pid": 3, "nome": "Spotify", "memoria": 150}
]

high_process = [process["nome"] for process in processos if process["memoria"]> 200]

print(high_process)

