'''Exercício com Classes
1 - Crie uma classe Carro (Nome)
2 - Crie um classe Motor (Nome)
3 - Crie uma classe Fabricante (Nome)
4 - Faça ligação entre carro e Motor
Obs.: Um motor pode ser de vários carros
5 - Faça a ligação entre Carro e Fabricante
Obs.: Um fabricante pode fabricar vários carros
Exiba o nome do carro, motor e fabricantes na tela
'''

class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante


    def informacoes(self):
        print(self.nome, self.motor.nome, self.fabricante.nome, sep=' ', end='\n')

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

class Garagem:
    def __init__(self):
        self._carros = []
    
    def insere_carro(self, carro):
        self._carros.append(carro)

    def lista_carros(self):
        for carro in self._carros:
            carro.informacoes()

def cria_carro(nome, motor, fabricante):
    return Carro(nome, motor, fabricante)

garagem = Garagem()

motor1 = Motor('2.0')
motor2 = Motor('1.0')

fabricante1 = Fabricante('Toyota')
fabricante2 = Fabricante('Audi')
Fabricante3 = Fabricante('Fiat')

carro1 = cria_carro('Corolla', motor1, fabricante1)
garagem.insere_carro(carro1)
carro2 = cria_carro('A4', motor1, fabricante2)
garagem.insere_carro(carro2)
carro3 = cria_carro('Uno', motor2, Fabricante3)
garagem.insere_carro(carro3)
garagem.lista_carros()