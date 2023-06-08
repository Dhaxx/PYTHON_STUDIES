'''CRIE UMA FUNÇÃO QE RETORNA SE UM NÚMERO É PAR OU ÍMPAR'''

def par_ou_impar(num):
    resto = num % 2
    if resto == 0:
        return f"{num} é Par"
    else:
        return f"{num} é Ímpar"

num = int(input('Digite um número: '))    
print(par_ou_impar(num))