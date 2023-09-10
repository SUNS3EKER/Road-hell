#distribucion de area de juego x=950

# import the pygame module
import pygame
import os

# Dimensiones de la pnatalla
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

screen = pygame.display.set_mode((1300,650))

#todo balas
# Set the caption of the screen
pygame.display.set_caption("Road Hell")


# Variable to keep our game loop running

carretera = pygame.image.load("./carretera.png")
carretera2 = pygame.image.load("./carretera.png")
mar = pygame.image.load("./mar.png")
mar2 = pygame.image.load("./mar.png")

velocidadbg = 6
running = True
carreteraxpos = 0
xpos = 500
carreteraypos = 0
carretera2ypos = 0-screen.get_height()
marypos = 0
mar2ypos = 0 - screen.get_height()

ypos = 50
# textura del jugador
jugador = pygame.image.load("./player.png")
#textura del NPCs
NPCcar = pygame.image.load("./npccar.png")
NPCcar2 = pygame.image.load("./npccar.png")




# variables de movimiento
moverarriba = False
moverabajo = False
moverD = False
moverI = False
velocidad = 5
# reloj   

reloj = pygame.time.Clock()
fps = 30
#* game loop
while running:

    reloj.tick(fps)


    #movimiento del fondo
    carreteraypos += velocidadbg
    carretera2ypos += velocidadbg
    if carreteraypos > screen.get_height():
      carreteraypos = 0 - screen.get_height()
    elif carretera2ypos > screen.get_height():
      carretera2ypos = 0 - screen.get_height()

    marypos += 3
    mar2ypos += 3
    if marypos > screen.get_height():
     marypos = 0 - screen.get_height()
    if mar2ypos > screen.get_height():
     mar2ypos = 0 - screen.get_height()
    # aumento a la posicion del jugador
    if moverD == True:
        xpos += velocidad
    if moverI == True:
        xpos -= velocidad
    if moverarriba == True:
        ypos -= 5
    if moverabajo == True:
        ypos += 6
    # colision con los bordes de la pantalla
    if xpos <= 473:
        moverI = False
        xpos = 473 + 1
    if ypos <= 0:
        moverarriba = False
        ypos = 1
    if (xpos + jugador.get_width()) >= 840:
        moverD = False
        xpos = 840 - jugador.get_width()
    if (ypos + jugador.get_height()) >= screen.get_height():
        moverabajo = False
        ypos -= 1

    # el jugador moviendose

    screen.fill((255, 255, 255))
    screen.blit(carretera,(carreteraxpos,carreteraypos))
    screen.blit(carretera2,(carreteraxpos,carretera2ypos))
    screen.blit(mar,(0,marypos))
    screen.blit(mar2,(0,mar2ypos))
    
        #TODO NPCs#########################################trabajar aqui 
        #la posicion z(capa) de las imagenes depende de cual se blitea primero y ultimo


    screen.blit(jugador, (xpos, ypos))


    pygame.display.update()

    # ciclo de eventos
    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
        # movimiento a la derecha
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moverD = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moverD = False
        # movimiento a la izquierda
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moverI = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moverI = False
        # movimiento arriba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moverarriba = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                moverarriba = False
        # movimiento abajo
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                moverabajo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                moverabajo = False
