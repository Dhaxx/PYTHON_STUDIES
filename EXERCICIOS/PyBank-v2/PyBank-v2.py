import Operacoes

'''
1. CRIAR UM SISTEMA BANCÁRIO COM AS OPERAÇÕES: SACAR, DEPOSITAR, EXTRATO, CADASTRAR USUÁRIO E CADASTRAR CONTA 
2. SEPARAR EM FUNÇÕES
3. PERMITIR 3 SAQUES DIÁRIOS.
4. LIMITE MÁXIMO DE 500 POR SAQUE. 
5. CASO FALTE SALDO, O SISTEMA DEVE EXIBIR UMA MSG.
6. VALORES DEVEM SER EXIBIDOS COMO "R$ xxx.xx"
'''

menu = '''
[BEM-VINDO AO PYBANK]

(1) SACAR
(2) DEPOSITAR
(3) EXTRATO
(4) CADASTRAR USUÁRIO
(5) CADASTRAR CONTA CORRENTE
(6) LISTAR CONTAS CORRENTES
(7) SAIR

ESCOLHA UMA OPERAÇÃO:
'''

saldo_conta = 0
LIMITE_DE_SAQUES = 3
VALOR_POR_SAQUE = 500

while True:
    operacao = int(input(menu))

    if operacao == 1: # SACAR
        valor_de_saque = int(input('Digite o Valor que deseja retirar: '))
        saldo_conta = Operacoes.sacar(limite_de_saque = LIMITE_DE_SAQUES, limite_de_valor = VALOR_POR_SAQUE, valor = valor_de_saque, saldo = saldo_conta)
        
    elif operacao == 2: # DEPOSITAR
        try:
            valor_deposito = int(input("Digite o valor do depósito: "))
            saldo_conta = Operacoes.depositar(valor_deposito, saldo_conta)
        except:
            print("OPERAÇÃO CANCELADA!")

    elif operacao == 3:
        Operacoes.extrato(saldo_conta, movimentacoes = Operacoes.transacoes)

    elif operacao == 4:
        print(5*"=" + "CRIAÇÃO DE USUÁRIO" + 5*"=")
        nome = str(input("Nome Completo: ")).title()
        data = input("Data de Nascimento (Somente Números): ")
        data = f"{data[:2]}-{data[2:4]}-{data[4:]}"
        cpf = int(input("CPF (Apenas Números): "))
        logradouro = str(input("Logradouro: ")).capitalize()
        numero = int(input("Numero: "))
        bairro = str(input("Bairro: ")).capitalize()
        cidade = str(input("Cidade: ")).capitalize()
        sigla = str(input("Sigla/Estado: ")).upper()
        endereco = logradouro,' ', numero, '-', bairro, '-', cidade,'/',sigla

        Operacoes.criar_usuario(nome, data, cpf=cpf, endereco=endereco)

    elif operacao == 5:
        print(5*"=" + "CRIAÇÃO DE CONTA CORRENTE" + 5*"=")
        cpf = int(input("Digite o CPF do Usuário: "))

        Operacoes.criar_contaCorrente('0001', cpf)

    elif operacao == 6:
        cpf = int(input("Digite o CPF do Usuário: "))
        Operacoes.listar_contasCorrente(cpf)

    elif operacao == 7:
        print("OBRIGADO POR CONFIAR EM NOSSOS SERVIÇOS!")
        break
        
    else:
        print("OPERAÇÃO INVÁLIDA!")