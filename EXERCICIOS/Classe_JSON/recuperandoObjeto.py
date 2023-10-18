from criandoClasse import Carro
import json

with open('./Classe_JSON/dados_carro.json', 'r') as f:
    carros = json.load(f)
    c1 = Carro(**carros)
    print(c1.nome)