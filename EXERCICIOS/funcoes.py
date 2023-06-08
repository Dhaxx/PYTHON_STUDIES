'''CRIE UMA FUNÇÃO QUE MULTIPLICA TODOS OS ARGUMENTOS NÃO NOMEADOS RECEBIDOS
RETORNE O TOTAL PARA UMA VAR E MOSTRE O VALOR DA VARIÁVEL'''

# def multiplicacao(*args):
#     multi = 1
#     for arg in args:
#         multi *= arg
#     return multi

# result_multiplicacao = multiplicacao(1, 2, 3, 4, 5, 6)

'''CRIE FUNÇÕES QUE DUPLICAM, TRIPLICAM E QUADRUPLICAM O NÚMERO RECEBIDO'''
def numero_base(num):
    def multiplicador(mult):
        return  f"{num} X {mult}: {num*mult}"
    return multiplicador

multiplicando = numero_base(5)
duplicado = multiplicando(2)
triplicado = multiplicando(3)
quadruplicado = multiplicando(4)

print(
    multiplicando(2),
    multiplicando(3),
    multiplicando(4),
    sep='\n'
)