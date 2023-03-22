import matplotlib.pyplot as plt

def draw_line_DDA(x1, y1, x2, y2):
    # calcula a diferença entre as coordenadas x e y
    dx = x2 - x1
    dy = y2 - y1
    
    # determina o número de passos a serem tomados
    steps = max(abs(dx), abs(dy))
    
    # calcula o incremento a ser aplicado em cada passo
    x_increment = dx / float(steps)
    y_increment = dy / float(steps)
    
    # desenha a linha, traçando uma linha que conecta os pontos gerados pelo algoritmo DDA
    x = x1
    y = y1
    plt.plot([round(x)], [round(y)], 'gx')
    
    for i in range(int(steps)):
        x += x_increment
        y += y_increment
        plt.plot([round(x)], [round(y)], 'gx')
    
    plt.plot([x1, x2], [y1, y2], 'b-')  # desenha a linha conectando os pontos gerados pelo algoritmo DDA
    
    # mostra o resultado na tela
    plt.axis([0, 50, 0, 50])
    plt.show()

# exemplo de uso
draw_line_DDA(1, 1, 8, 5)

def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    err = dx - dy
    
    while x0 != x1 or y0 != y1:
        yield x0, y0
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    
    yield x0, y0
    

# Exemplo de uso
import matplotlib.pyplot as plt

# Define os pontos iniciais e finais da reta
x0, y0 = 1, 1
x1, y1 = 10, 5

# Chama a função que aplica o algoritmo de Bresenham
line = list(bresenham_line(x0, y0, x1, y1))

# Plota a reta
plt.plot([p[0] for p in line], [p[1] for p in line])

plt.show()
