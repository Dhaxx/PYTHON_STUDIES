import os

'''
Faça uma lista de compras com listas
O usuário deve ter a possiblidade de inserir,
apagar e listar valores da sua lista
Não permita que o programa quebre com erros
de índices inexistentes na lista
'''

lista = []
produto = ''
indice = ''

while True:
    print("\n")
    try:
        print(5*'=', 'Minha Lista', 5*'=')
        print('1 - Inserir na lista')
        print('2 - Remover da lista')
        print('3 - Exibir lista')
        print('4 - Sair')
        opcao = int(input('Digite uma opção: '))
        
        if opcao == 1:
            while True:
                produto = str(input('Qual o nome do produto: ')).capitalize()
                if produto != '':
                    lista.append(produto)  
                    print('Produto Adicionado a sua lista!')
                elif produto == "":
                    break
                else:
                    print('Nome não pode ser vazio!')
                    continue
        elif opcao == 2:
            while True:
                for i, item in enumerate(lista):
                    print(f'{i} {item}')
                if len(lista) > 0:
                    try:
                        indice = int(input('Digite o índice do item que deseja excluir: '))
                        lista.pop(indice)
                        print('Item removido!')
                        break
                    except:
                        print('Índice inexistente!')
                        continue
                else:
                    print('Sua lista está vazia!')
                    break
        elif opcao == 3:
                if len(lista) == 0:
                    print('Sua lista está vazia!')
                else:
                    for i, item in enumerate(lista):
                        print(f'{i} {item}')  
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print('Opção Inválida!!!')
            continue
    except:
        os.system('cls')
        continue