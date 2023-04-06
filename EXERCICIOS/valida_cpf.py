###  VALIDANDO CPF ###
digitos_somados = 0
cpf = (input('Insira o CPF: ').replace('.','')).replace('-','')
i = 10

# Primeira validação
for numero in cpf[:9]: 
    digito_multiplicado = int(numero) * i
    digitos_somados += digito_multiplicado
    i -= 1

digito = (digitos_somados * 10) % 11
digito_validador1 = 0 if digito > 9 else digito 

print(digito_validador1)