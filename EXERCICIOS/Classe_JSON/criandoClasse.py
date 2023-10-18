import json

class Carro:
    def __init__(self, nome, ligado=False):
        self.nome = nome
        self.ligado = True

    def ligar_ou_desligar(self):
        if self.ligado:
           self.ligado = False
           print (f'{self.nome} desligado!')
        else:
            self.ligado = True
            print(f'{self.nome} ligado')
    
    def acelerar(self):
        if self.ligado:
            print(f'{self.nome} está acelerando!')
        else:
            print(f'{self.nome} está desligado!')
    
    def frear(self):
        if self.ligado:
            print(f'{self.nome} está freando!')

carro1 = Carro('Corolla')

with open('./Classe_JSON/dados_carro.json', 'w') as f:
    json.dump(carro1.__dict__, f, ensure_ascii=False, indent=2) #Serializa os atributos do carro1 no JSON