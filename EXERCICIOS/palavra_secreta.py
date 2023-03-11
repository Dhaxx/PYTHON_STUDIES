from random import choice
import os

palavras = ['banana','amor','mae','sol','alegria','sonho']
palavra_aleatoria = choice(palavras)
letras_encontradas = ''
tentativas = 0

while True:
    tentativas += 1
    letra = str(input('Insira uma letra: ')).lower()
    
    if len(letra) == 1 and letra.isalpha():
        os.system('cls')
        palavra_formada = ''
        if letra in palavra_aleatoria:
            letras_encontradas += letra
        for x, l in enumerate(palavra_aleatoria):
            if l in letras_encontradas:
                print(l,end='')
                palavra_formada += l
            else:
                 print('*',end='')
        if palavra_formada == palavra_aleatoria: 
            print(f"\nVocê completou a palavra {palavra_aleatoria}. Parabéns!!!")
            break
    else:
        print("Insira um valor válido!!\n")
    print(f"\n{tentativas} Tentativa(s)")
