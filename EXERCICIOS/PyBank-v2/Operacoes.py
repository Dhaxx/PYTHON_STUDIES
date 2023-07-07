'''
1. DEVE RECEBER ARGUMENTOS APENAS POR NOME (KEYWORD ONLY) 
'''

saques_realizados = 0
extrato = []


def sacar(limite_de_saque, limite_de_valor, valor, saldo):
    global saques_realizados

    if saques_realizados < limite_de_saque:
        try:
            saldo_futuro = saldo - valor

            if (valor > 0 and valor <= limite_de_valor) and saldo_futuro > 0:
                saques_realizados += 1
                saldo = saldo_futuro
                print("SAQUE REALIZADO COM SUCESSO!")
                extrato.append('- R$' + format(valor, ".2f"))
                return saldo

            elif (valor > 0 and valor < limite_de_valor) and saldo_futuro < 0:
                print("OPERAÇÃO CANCELADA! O SALDO DA CONTA FICARÁ NEGATIVO.")

            elif valor > 0 and valor > limite_de_valor:
                print("OPERAÇÃO CANCELADA! O VALOR DE SAQUE ULTRAPASSA O LIMITE DE R$ 500.00 POR SAQUE")
        except:
            print("OPERAÇÃO CANCELADA")
    else:
        print("LIMITE DE 3 SAQUES DIÁRIOS FOI ATINGIDO. VOLTE AMANHÃ!")
        return saldo

def depositar():
    ...