import re
import math


def verificaForca(senha: str) -> dict:
    alfabeto = 0
    tem_minuscula = bool(re.search(r'[a-z]', senha))
    tem_maiuscula = bool(re.search(r'[A-Z]', senha))
    tem_numero    = bool(re.search(r'[0-9]', senha))
    tem_simbolo   = bool(re.search(r'[^a-zA-Z0-9]', senha))

    if tem_minuscula: alfabeto += 26
    if tem_maiuscula: alfabeto += 26
    if tem_numero:    alfabeto += 10
    if tem_simbolo:   alfabeto += 32

    if alfabeto == 0 or len(senha) == 0:
        entropia = 0
    else:
        entropia = len(senha) * math.log2(alfabeto)

    tem_sequencia = bool(re.search(r'(012|123|234|345|456|567|678|789|abc|bcd|cde)', senha.lower()))
    tem_repeticao = bool(re.search(r'(.)\1{2,}', senha))

    penalidade = 0
    if tem_sequencia: penalidade += 10
    if tem_repeticao: penalidade += 10

    entropia_efetiva = max(0, entropia - penalidade)

    if len(senha) < 4:
        nivel = "Muito fraca"
    elif entropia_efetiva < 36:
        nivel = "Fraca"
    elif entropia_efetiva < 60:
        nivel = "Razoável"
    elif entropia_efetiva < 128:
        nivel = "Forte"
    else:
        nivel = "Muito forte"

    dicas = []
    if not tem_maiuscula: dicas.append("Adicione letras maiúsculas")
    if not tem_numero:    dicas.append("Adicione números")
    if not tem_simbolo:   dicas.append("Adicione símbolos (!@#...)")
    if len(senha) < 12:   dicas.append("Use ao menos 12 caracteres")
    if tem_sequencia:     dicas.append("Evite sequências como '123' ou 'abc'")
    if tem_repeticao:     dicas.append("Evite caracteres repetidos seguidos")

    return {
        "nivel":         nivel,
        "tem_maiuscula": tem_maiuscula,
        "tem_numero":    tem_numero,
        "tem_simbolo":   tem_simbolo,
        "tem_sequencia": tem_sequencia,
        "tem_repeticao": tem_repeticao,
        "dicas":         dicas,
    }


def formata_resultado(resultado: dict) -> str:
    texto = f"Nível: {resultado['nivel']}"
    if resultado["dicas"]:
        texto += " | " + " | ".join(resultado["dicas"])
    return texto
