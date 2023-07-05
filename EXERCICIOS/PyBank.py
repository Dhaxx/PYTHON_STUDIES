'''
1. CRIAR UM SISTEMA BANCÁRIO COM AS OPERAÇÕES: SACAR, DEPOSITAR E EXTRATO
2. DEPOSITAR APENAS VALORES POSITIVOS
3. PERMITIR 3 SAQUES DIÁRIOS
4. LIMITE MÁXIMO DE 500 POR SAQUE. 
5. CASO FALTE SALDO, O SISTEMA DEVE EXIBIR UMA MSG.
6. VALORES DEVEM SER EXIBIDOS COMO "R$ xxx.xx"
'''

menu = '''
[BEM-VINDO AO PYBANK]

(1) SACAR
(2) DEPOSITAR
(3) EXTRATO
(4) SAIR

ESCOLHA UMA OPERAÇÃO:
'''

saldo = 0
saques_realizados = 0
extrato = []
LIMITE_DE_SAQUES = 3
VALOR_POR_SAQUE = 500

while True:
    operacao = int(input(menu))

    if operacao == 1: # SACAR
        if saques_realizados < LIMITE_DE_SAQUES:
            try:
                valor_do_saque = int(input("Digite o valor que deseja sacar: "))
                saldo_futuro = saldo - valor_do_saque

                if (valor_do_saque > 0 and valor_do_saque <= VALOR_POR_SAQUE) and saldo_futuro > 0:
                    saques_realizados += 1
                    saldo = saldo_futuro
                    print("SAQUE REALIZADO COM SUCESSO!")
                    extrato.append('- R$' + format(valor_do_saque, ".2f"))

                elif (valor_do_saque > 0 and valor_do_saque < VALOR_POR_SAQUE) and saldo_futuro < 0:
                    print("OPERAÇÃO CANCELADA! O SALDO DA CONTA FICARÁ NEGATIVO.")

                elif valor_do_saque > 0 and valor_do_saque > VALOR_POR_SAQUE:
                    print("OPERAÇÃO CANCELADA! O VALOR DE SAQUE ULTRAPASSA O LIMITE DE R$ 500.00 POR SAQUE")
            except:
                print("OPERAÇÃO CANCELADA!")
                
        else:
            print("VOCÊ JÁ REALIZOU 3 SAQUES HOJE! VOLTE AMANHÃ.")
        
    elif operacao == 2:
        try:
            valor_deposito = int(input("Digite o valor do depósito: "))
            
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato.append("+ R$" + format(valor_deposito, ".2f"))
        except:
            print("OPERAÇÃO CANCELADA! VALOR DE DEPÓSITO NÃO PERMITIDO.")

    elif operacao == 3:
        print(5*'=' + 'EXTRATO' + 5*'=')
        print(*extrato, sep="\n")
        print(f'SALDO ATUAL: R${saldo:.2f}')
    
    elif operacao == 4:
        print("OBRIGADO POR CONFIAR EM NOSSOS SERVIÇOS!")
        break

    else:
        print("OPERAÇÃO INVÁLIDA!")