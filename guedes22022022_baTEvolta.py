from vpython import *
#Web VPython 3.2

#paredes 
paredeEsquerda = box(pos=vector(-20, 0, 0), size=vector(0.5, 20, 0.5), color=color.red)
paredeDireita = box(pos=vector(20, 0, 0), size=vector(0.5, 20, 0.5), color=color.red)
teto = box(pos=vector(0, 10, 0), size=vector(40, 0.5, 0.5), color=color.red)
chao = box(pos=vector(0, -10, 0), size=vector(40, 0.5, 0.5), color=color.red)

#bolas
bola1 = sphere(pos=vector(0, 0, 0), radius=1, color=color.blue, make_trail=True)
bola2 = sphere(pos=vector(-5, -5, 0), radius=1, color=color.green, make_trail=True)
bola3 = sphere(pos=vector(5, 5, 0), radius=1, color=color.yellow, make_trail=True)

# movimentos das bolinha ze
velocidade1 = vector(15, 10, 0)
velocidade2 = vector(-10, 8, 0)
velocidade3 = vector(12, -7, 0)

while True:
    rate(60)
    
    # atualiza as posicao com pase na velocidade, obs: elas iniciam sempre no mesmo ponto de partida
    bola1.pos += velocidade1 * 0.01
    bola2.pos += velocidade2 * 0.01
    bola3.pos += velocidade3 * 0.01
    
    #colisão com parede/inverte a direção
    if abs(bola1.pos.x) >= 20 - bola1.radius:
        velocidade1.x *= -1
    if abs(bola1.pos.y) >= 10 - bola1.radius:
        velocidade1.y *= -1

    if abs(bola2.pos.x) >= 20 - bola2.radius:
        velocidade2.x *= -1
    if abs(bola2.pos.y) >= 10 - bola2.radius:
        velocidade2.y *= -1

    if abs(bola3.pos.x) >= 20 - bola3.radius:
        velocidade3.x *= -1
    if abs(bola3.pos.y) >= 10 - bola3.radius:
        velocidade3.y *= -1

    # Verifica colisão entre as bolas (trocando as velocidades)
    if mag(bola1.pos - bola2.pos) <= bola1.radius + bola2.radius:
        velocidade1, velocidade2 = velocidade2, velocidade1
        
    if mag(bola1.pos - bola3.pos) <= bola1.radius + bola3.radius:
        velocidade1, velocidade3 = velocidade3, velocidade1
        
    if mag(bola2.pos - bola3.pos) <= bola2.radius + bola3.radius:
        velocidade2, velocidade3 = velocidade3, velocidade2
