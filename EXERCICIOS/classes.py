''' 1. Classe Bola: Crie uma classe que modele uma bola
    a - Atributos: Cor, circunferência, material
    b - Métodos: trocaCor e mostraCor'''
# class Bola:
#     def __init__(self, cor, circunferencia, material):
#         self._cor = cor
#         self.circunferencia = circunferencia
#         self.material = material

#     @property
#     def cor(self): # Getter
#         return self._cor
    
#     @cor.setter
#     def cor(self, value): # Setter
#         self._cor = value
#         return self._cor
    
# b1 = Bola('branco', 60, 'capotão')
# print('cor atual' + b1.cor)
# print('alterando...')
# b1.cor = 'Vermelho'
# print('cor atual' + b1.cor)

'''2. Classe Quadrado: Crie uma classe que modele um quadrado:
    a.Atributos: Tamanho do lado
    b.Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;'''
# class Quadrado:
#     def __init__(self, tamanho):
#         self._tamanho_lado = tamanho

#     @property
#     def lado(self):
#         return self._tamanho_lado
    
#     @lado.setter
#     def lado(self, lado):
#         self._tamanho_lado = lado
#         return self._tamanho_lado
    
#     def calcula_area(self):
#         area = self.lado ** 2
#         return area
    
# quadrado = Quadrado(3)
# print('Lado Atual: ', quadrado.lado)
# print(f'Área Atual: {quadrado.calcula_area()}m²')
# quadrado.lado = 5
# print('Lado Atual: ', quadrado.lado)
# print(f'Área Atual: {quadrado.calcula_area()}m²')

'''3. Classe Retangulo: Crie uma classe que modele um retangulo:
    a.Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    b.Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    c.Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois,
      deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.'''