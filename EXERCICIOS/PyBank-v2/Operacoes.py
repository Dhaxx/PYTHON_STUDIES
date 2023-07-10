'''
ADICIONAR SALDOS/LIMITES/EXTRATOS POR CONTA CORRENTES
'''

saques_realizados = 0
contador_conta = 0
transacoes = []
usuarios = [{'nome': 'Kaio Pablo Martins', 'data_nascimento': '09-01-2003', 'cpf': 14547882673, 'endereco': ('Teste', ' ', 80, '-', 'Teste', '-', 'Teste', '/', 'SP')},
            {'nome': 'Beatriz Oliveira Cassin', 'data_nascimento': '08-09-2005', 'cpf': 99999999999, 'endereco': ('Teste', ' ', 80, '-', 'Teste', '-', 'Teste', '/', 'SP')}]
contas_correntes = []

def sacar(limite_de_saque, limite_de_valor, valor, saldo):
    global saques_realizados

    if saques_realizados < limite_de_saque:
        try:
            saldo_futuro = saldo - valor

            if (valor > 0 and valor <= limite_de_valor) and saldo_futuro >= 0:
                saques_realizados += 1
                saldo = saldo_futuro
                print("SAQUE REALIZADO COM SUCESSO!")
                transacoes.append('- R$' + format(valor, ".2f"))
                return saldo

            elif (valor > 0 and valor < limite_de_valor) and saldo_futuro < 0:
                print("OPERAÇÃO CANCELADA! O SALDO DA CONTA FICARÁ NEGATIVO.")
                return saldo

            elif valor > 0 and valor > limite_de_valor:
                print("OPERAÇÃO CANCELADA! O VALOR DE SAQUE ULTRAPASSA O LIMITE DE R$ 500.00 POR SAQUE")
                return saldo
        except:
            print("OPERAÇÃO CANCELADA")
    else:
        print("LIMITE DE 3 SAQUES DIÁRIOS FOI ATINGIDO. VOLTE AMANHÃ!")
        return saldo

def depositar(valor, saldo):
    try:
        if valor > 0:
            saldo += valor
            transacoes.append("+ R$" + format(valor, ".2f"))
            print("OPERAÇÃO REALIZADA COM SUCESSO!")
            return saldo
    except:
        print("OPERAÇÃO CANCELADA! VALOR DE DEPÓSITO NÃO PERMITIDO.")

def extrato(saldo, movimentacoes):
    print(5*'=' + 'EXTRATO' + 5*'=')
    print(*movimentacoes, sep="\n")
    print(f'SALDO ATUAL: R${saldo:.2f}')
    print(10*'=')

def criar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("OPERAÇÃO CANCELADA! USUÁRIO JÁ CADASTRADO")
            return

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("USUÁRIO CADASTRADO COM SUCESSO!")

def criar_contaCorrente(agencia, cpf):
    global contador_conta
    contador_conta += 1

    for usuario in usuarios:
        print(usuario["cpf"])
        if usuario["cpf"] == cpf:
            conta_corrente = {
                "agencia": agencia,
                "numero_conta": contador_conta,
            }
            usuario.setdefault("contas", []).append(conta_corrente)
            print("Conta corrente criada e associada ao usuário com sucesso!")
            break
    else:
        print("CPF não encontrado. A conta corrente não pode ser criada.")

def listar_contasCorrente(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Nome:", usuario["nome"])
            print(5*'=',"Contas Correntes:",5*'=')
            for conta in usuario.get("contas", []):
                print("Agência:", conta["agencia"])
                print("Número da Conta:", conta["numero_conta"])
                print()
            break
    else:
        print("CPF não encontrado. Não há contas correntes para listar.")

