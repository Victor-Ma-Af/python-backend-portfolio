#Exerc 2 the Duel
class Personagem:
    def __init__(self, name: str, life: int):
        self.name = name
        self.life = life
    def take_damage(self, dano: int):
        self.life -= dano
        if self.life <= 0:
            self.life = 0
        return f"{self.name} recebeu {dano}. Vida atual: {self.life}"
    def attack(self, target: Personagem, dano: int):
        return f"{self.name} atacou {target.name}, {target.take_damage(dano)}"

agent_1 = Personagem("Omen", 100)
agent_2 = Personagem("Jett", 100)

print(agent_1.attack(agent_2, 40))
