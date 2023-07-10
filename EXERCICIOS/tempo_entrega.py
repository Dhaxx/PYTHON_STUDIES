'''[TEMPO DE ENTREGA]'''
# while True:
#     nomeRestaurante = input()
#     tempoEstimadoEntrega = int(input())

#     print(f'O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos.')

'''[TOTAL DE PEDIDO + TROCO]'''
# valorHamburguer = float(input())
# quantidadeHamburguer = int(input())
# valorBebida = float(input())
# quantidadeBebida = int(input())
# valorPago = float(input())
# total_hamburgueres = 0
# total_bebidas = 0
# valor_final = 0

# total_hamburgueres = valorHamburguer * quantidadeHamburguer
# total_bebidas = valorBebida * quantidadeBebida
# valor_final = total_hamburgueres + total_bebidas

# troco = valorPago - valor_final

# print(f"O preço final do pedido é R$ {float(valor_final):.2f}. Seu troco é R$ {float(troco):.2f}.")

# '''[GANHE UMA SOBREMESA]'''

# valorPedido = int(input())

# if valorPedido >= 50.00:
#     print("Parabens, você ganhou uma sobremesa gratis!")
# else:
#     print('Que pena, você nao ganhou nenhum brinde especial.')

'''[PEDIDO ONLINE COM DESCONTO]'''
# def main():
#     n = int(input())
 
#     total = 0
 
#     for i in range(1, n + 1):
#         pedido = input().split(" ")
#         nome = pedido[0]
#         valor = float(pedido[1])
#         total += valor
 
#     desconto = input()

#     if desconto == '10%':
#         print(f"Valor total: {total - (total * 0.10):.2f}")
#     else: 
#         print(f"Valor total: {total - (total * 0.20):.2f}")
 
 
# if __name__ == "__main__":
#     main()

'''[PEDIDOS VEGANOS]'''
# numPedidos = int(input())
# pedidos = []

# for i in range(1, numPedidos + 1):
#     prato = input()
#     calorias = int(input())
#     vegano = input('')
#     ehVegano = 'Nao-vegabo' if vegano == 'n' else 'Vegano'

#     pedidos.append(f'Pedido {i}: {prato} ({ehVegano}) - {calorias} calorias')

# print(*pedidos, sep='\n')
