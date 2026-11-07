import sys
from ui.janela import build_gui
from senha.gerador import geraSenha
from senha.forca import verificaForca, formata_resultado
from senha.constantes import total_senhas


def main_console():
    print("Quantidade total de senhas:", total_senhas)
    senha = geraSenha()
    print("Senha gerada:", senha)
    print("Força da senha:", formata_resultado(verificaForca(senha)))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "--cli":
        main_console()
    else:
        if not build_gui():
            print("Executando no modo console como alternativa.")
            main_console()
