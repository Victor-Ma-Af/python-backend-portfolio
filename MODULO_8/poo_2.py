#Desafio
class Usuario:
    def __init__(self, id: int, name: str, email:str):
        self.id = id
        self.name = name
        self.email = email 
    def to_dict(self):
        return  {
                    "id": id,
                    "name": name,
                    "email": email
                }

victor = Usuario(29, "victor", "dotor5470@gmail.com")
victor_dict = victor.to_dict

print(victor.to_dict)
print(victor_dict())
print(Usuario.to_dict(victor))
