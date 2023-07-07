import Operacoes

'''
1. CRIAR UM SISTEMA BANCÁRIO COM AS OPERAÇÕES: SACAR, DEPOSITAR, EXTRATO, CADASTRAR USUÁRIO E CADASTRAR CONTA 
2. SEPARAR EM FUNÇÕES
3. PERMITIR 3 SAQUES DIÁRIOS.
4. LIMITE MÁXIMO DE 500 POR SAQUE. 
5. CASO FALTE SALDO, O SISTEMA DEVE EXIBIR UMA MSG.
6. VALORES DEVEM SER EXIBIDOS COMO "R$ xxx.xx"
7. DEPÓSITO DEVE RECEBER ARGUMENTOS APENAS POR POSIÇÃO (POSITION ONLY)
'''

menu = '''
[BEM-VINDO AO PYBANK]

(1) SACAR
(2) DEPOSITAR
(3) EXTRATO
(4) SAIR

ESCOLHA UMA OPERAÇÃO:
'''

saldo_conta = 1000
LIMITE_DE_SAQUES = 3
VALOR_POR_SAQUE = 500

while True:
    operacao = int(input(menu))

    if operacao == 1: # SACAR
        valor_de_saque = int(input('Digite o Valor que deseja retirar: '))
        saldo_conta = Operacoes.sacar(limite_de_saque = LIMITE_DE_SAQUES, limite_de_valor = VALOR_POR_SAQUE, valor = valor_de_saque, saldo = saldo_conta)
        
    elif operacao == 2: # DEPOSITAR
        ...
    #     try:
    #         valor_deposito = int(input("Digite o valor do depósito: "))
            
    #         if valor_deposito > 0:
    #             saldo += valor_deposito
    #             extrato.append("+ R$" + format(valor_deposito, ".2f"))
    #     except:
    #         print("OPERAÇÃO CANCELADA! VALOR DE DEPÓSITO NÃO PERMITIDO.")

    elif operacao == 3:
        print(5*'=' + 'EXTRATO' + 5*'=')
        print(*Operacoes.extrato, sep="\n")
        print(f'SALDO ATUAL: R${saldo_conta:.2f}')
    
    # elif operacao == 4:
    #     print("OBRIGADO POR CONFIAR EM NOSSOS SERVIÇOS!")
    #     break

    else:
        print("OPERAÇÃO INVÁLIDA!")