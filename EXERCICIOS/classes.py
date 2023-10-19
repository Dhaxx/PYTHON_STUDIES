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

# # Constantes 
# AREA_PISO = 1 
# LARGURA_RODAPE = 0.1

# class Retangulo:
#     def __init__(self, base, altura):
#         self._base = base
#         self._altura = altura

#     @property
#     def base(self):
#         return self._base
    
#     @base.setter
#     def base(self, value):
#         self._base = value
    
#     @property
#     def altura(self):
#         return self._altura
    
#     @altura.setter
#     def altura(self, value):
#         self._altura = value
    
#     def area(self):
#         return self._base * self._altura
    
#     def perimetro(self):
#         return 2 * (self._base + self._altura)

# base = float(input('Insira a medida da base: '))
# altura = float(input('Insira a medida da altura: '))

# retangulo = Retangulo(base, altura)
# print(f'Base: {retangulo.base:.2f}')
# print(f'Altura: {retangulo.altura:.2f}')

# quantidade_de_pisos = retangulo.area() / AREA_PISO
# quantidade_de_rodapes = retangulo.perimetro() * LARGURA_RODAPE

# print(f'A quantidade de Pisos é: {quantidade_de_pisos:.2f}')
# print(f'A quantidade de Rodapés é: {quantidade_de_rodapes:.2f}')

'''Classe Pessoa: Crie uma classe que modele uma pessoa:
    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.'''

# class Pessoa:
#     def __init__(self, nome, idade, peso, altura):
#         self.nome = nome          
#         self.idade = idade
#         self.peso = float(peso)
#         self.altura = altura

#     def envelhecer(self):
#         self.idade += 1

#     def crescer(self):
#         if self.idade <= 21:
#             self.crescer += 0.5

#     def engordar(self):
#         self.peso += 1.0

#     def emagrecer(self):
#         self.peso -= 1.0

''''''