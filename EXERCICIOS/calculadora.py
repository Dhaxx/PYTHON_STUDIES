'''
Esse foi o programa que montei para solucionar a tarefa proposta em aula pelo professor
na aula número 66 do Curso de Python 3 do Básico Ao Avançado - Exercício guiado - Calculadora
na plataforma da Udemy Academy.

By: Kaio Pablo Martins
'''

executando = True

def menu():
    print("===ESCOLHA A OPERAÇÃO DESEJADA===")
    print("(+) SOMA")
    print("(-) SUBTRAÇÃO")
    print("(*) MULTIPLICAÇÃO")
    print("(/) DIVISÃO")
    print("(^) EXPONENCIAÇÃO")
    print("(@) Mudar Valor")
    print("(S) SAIR")
    opcao = str(input(''))
    return opcao

while executando:
    opcao = ...
    try:
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))
    except:
        print("DIGITE UM VALOR DO TIPO NÚMERICO")
        continue
    
    while opcao != 'S':
        opcao = menu()
        if opcao == '+':
            print(f"{numero1} + {numero2} = {numero1 + numero2}")
        elif opcao == '-':
            print(f"{numero1} - {numero2} = {numero1 - numero2}")
        elif opcao == '*':
            print(f"{numero1} x {numero2} = {numero1 * numero2}")
        elif opcao == '/':
            print(f"{numero1} / {numero2} = {numero1 / numero2}")
        elif opcao == '^':
            print(f"{numero1} ^ {numero2} = {numero1 ** numero2}")
        elif opcao == 'S':
            print(f"Até a próxima...")
            executando = False
        elif opcao == "@":
            break
        else:
            print("OPÇÃO INVÁLIDA!")

    