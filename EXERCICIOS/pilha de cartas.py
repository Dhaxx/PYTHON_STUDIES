while True:
    try:
        num = int(input('Insira um Número: '))
    except:
        break
    
    cartas = [i for i in range(num, 0, -1)]
    
    while len(cartas) >= 2:
        cartas.pop() # Remove o Primeiro Número
        cartas.insert(0, cartas.pop()) # Remove o Primeiro Número e Coloca no Final
    print(cartas)