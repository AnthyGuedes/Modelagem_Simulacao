Web VPython 3.2

def calcular_y(pos_x, r):
    return sqrt(r**2 - (pos_x - 10)**2) + 10

# Inicialização dos objetos
planeta = sphere(pos=vector(10, 10, 0), radius=4, color=vector(0, 1, 0))  # Cor verde e tamanho reduzido
bola = sphere(pos=vector(10, 0, 10), radius=1, color=vector(1, 1, 1), make_trail=True)  
bola2 = sphere(pos=vector(30, 0, 0), radius=1, color=vector(0, 10, 2))  

# Direção de movimento para a PRIMEIRA bola
direcao1 = 1
x1 = 0

# Direção de movimento para a SEGUNDA bola
direcao2 = 1
x2 = 0

while True:
    rate(40) 
    
    # Movimento do planeta
    planeta.pos.z += 0.1
    
    # Calcula a posição y da bola1 com base na coordenada x
    if direcao1 < 0:
        y1 = 20 - calcular_y(x1, 10)
    else:
        y1 = calcular_y(x1, 10)
    
    # Atualiza a posição da bola1
    bola.pos.x = x1
    bola.pos.y = y1
    bola.pos.z += 0.1
    
    # Atualiza a posição da bola2
    bola2.pos.x = x2
    bola2.pos.y = y1
    bola2.pos.z += 0.1
    
    # Atualiza a coordenada x da bola1 e inverte a direção ao atingir os limites
    x1 += direcao1
    if x1 >= 20 or x1 <= 0:
        direcao1 *= -1
    
    # Atualiza a coordenada x da bola2 e inverte a direção ao atingir os limites
    x2 += direcao2
    if x2 >= 20 or x2 <= 0:
        direcao2 *= -1
