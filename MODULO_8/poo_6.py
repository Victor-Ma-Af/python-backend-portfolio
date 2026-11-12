'''Exercício 3 — Servidor e estados
Crie uma classe Servidor com nome, ip, memoria_gb e ligado = False.

Implemente ligar(), desligar() e status().

Desafio: impeça que um servidor já ligado seja ligado novamente e crie uma lista de servidores para verificar quais estão ativos.'''
class Servidor:
    def __init__(self, name, ip, gb_memory):
        self.name = name
        self.ip = ip
        self.gb_memory = gb_memory
        self.on = False
    def power_on(self):
        if self.on != True:
            self.on = True
            return f"Server on"
        else:
            return f"Server already on"
    def power_off(self):
        if self.on != False:
            self.on = False
            return f"Server off"
        else:
            return f"Serve already off"
    def stats(self):
        if self.on == True:
            return f"Server on"
        else:
            return f"Server off"

lab_1 = Servidor("host22", "192.168.0.10", 10)

