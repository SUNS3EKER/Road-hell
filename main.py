#distribucion de area de juego x=950

# import the pygame module
import pygame
import os
import math
import random
import time

# Dimensiones de la pnatalla
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)


# Set the caption of the screen
pygame.display.set_caption("Road Hell")


# Variable to keep our game loop running

carretera = pygame.image.load("./carretera.png")
carretera2 = pygame.image.load("./carretera2.png")
mar = pygame.image.load("./mar.png")
mar2 = pygame.image.load("./mar2.png")

velocidadbg = 5.5
running = True
carreteraxpos = (screen.get_width()/3)
xpos = carreteraxpos + (carreteraxpos/2)
carreteraypos = 0
carretera2ypos = 0-screen.get_height()
marypos = 0
mar2ypos = 0 - screen.get_height()

ypos = 50
# textura del jugador
jugador = pygame.image.load("./player.png")
#textura del NPCs
NPCcar = pygame.image.load("./npccar.png")

carril1 = {
    "existe":random.choice([False,True]),
    "posicion":(carreteraxpos,screen.get_height()),
    "Enemigo":False,
    "modelo":1
}



# variables de movimiento
moverarriba = False
moverabajo = False
moverD = False
moverI = False
velocidad = 4
# reloj
reloj = pygame.time.Clock()
fps = 60
# game loop
while running:

    reloj.tick(fps)
    #NPCs#########################################trabajar aqui
    if carril1["existe"] == True:
            screen.blit(NPCcar,(carreteraxpos,screen.get_height()))


    #movimiento del fondo
    carreteraypos += velocidadbg
    carretera2ypos += velocidadbg
    if carreteraypos > screen.get_height():
      carreteraypos = 0 - screen.get_height()
    if carretera2ypos > screen.get_height():
      carretera2ypos = 0 - screen.get_height()

    marypos += 2
    mar2ypos += 2
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
        ypos -= 4
    if moverabajo == True:
        ypos += 5
    # colision con los bordes de la pantalla
    if xpos <= carreteraxpos:
        moverI = False
        xpos = carreteraxpos + 1
    if ypos <= 0:
        moverarriba = False
        ypos = 1
    if (xpos + jugador.get_width()) >= (carreteraxpos+carretera.get_width()):
        moverD = False
        xpos = (carreteraxpos+carretera.get_width()) - jugador.get_width()
    if (ypos + jugador.get_height()) >= screen.get_height():
        moverabajo = False
        ypos -= 1

    # el jugador moviendose

    screen.fill((255, 255, 255))
    screen.blit(carretera,(carreteraxpos,carreteraypos))
    screen.blit(carretera2,(carreteraxpos,carretera2ypos))
    screen.blit(mar,(0,marypos))
    screen.blit(mar2,(0,mar2ypos))
    
    
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
