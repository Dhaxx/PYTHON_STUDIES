# Exercício - sistema de perguntas e respostas
pontuacao = 0


perguntas = [
    {
    'Pergunta': 'Quanto é 2+2?',
    'Opções': ['1','2','3','4','5'],
    'Resposta': '4',
    },
    {
    'Pergunta': 'Quanto é 5*5?',
    'Opções': ['25','10','5','30','15'],
    'Resposta': '25',  
    },
    {
    'Pergunta': 'Quanto é 10/2?',
    'Opções': ['25','10','5','30','15'],
    'Resposta': '5',  
    },
    {
    'Pergunta': 'Quanto é 30-8?',
    'Opções': ['28','10','5','30','22'],
    'Resposta': '22',  
    }]

for x in perguntas:
    print(x['Pergunta'])
    for i, opcao in enumerate(x['Opções']):
        print(f'{i}) {opcao}')
    resposta = int(input('Escolha a resposta: '))

    print(x['Opções'][resposta])

    if x['Opções'][resposta] == x['Resposta']:
        print("✔️ ACERTOU!",end="\n\n")
        pontuacao += 1
    else:
        print("❌ ERROU!",end="\n\n")

print(f'Sua pontuação foi {pontuacao}')
    




