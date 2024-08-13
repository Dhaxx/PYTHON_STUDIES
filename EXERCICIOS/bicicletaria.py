class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print('Bi Bi...')

    def parar(self):
        print('Freando...')

    def correr(self):
        print('Acelerando...')

    def __str__(self):
        return f"\nBicicleta: {self.cor} - {self.modelo} - {self.ano} - {self.valor}"


bike = Bicicleta('Azul', 'Caloi', 2024, 624.00)
bike.correr()
bike.parar()
bike.buzinar()
print(bike)