from random import randint
###  GERANDO CPF ###
cpf = ''
for x in range(9):
    cpf += str(randint(0, 9))

i = 10
digitos_somados = 0

# Primeira validação
for numero in cpf[:9]: 
    digito_multiplicado = int(numero) * i
    digitos_somados += digito_multiplicado
    i -= 1
digito = (digitos_somados * 10) % 11
digito_validador1 = '0' if digito > 9 else str(digito)

################################
i = 11
digitos_somados = 0
###############################
# Segunda validação
for numero in (cpf + digito_validador1):
    digito_multiplicado = int(numero) * i
    digitos_somados += digito_multiplicado
    i -= 1
digito = (digitos_somados * 10) % 11
digito_validador2 = 0 if digito > 9 else digito

print(cpf + str(digito_validador1) + str(digito_validador2))