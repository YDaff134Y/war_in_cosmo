import pygame, sys
import numpy as np
from pygame.locals import *


#class Player:

    
    

#class Right:
    


#class Left:



#class Propulsion:


#class Shoot:



#class Comets:



#class Start_Screen:

    

#class Final:

     

#class Colision:

    

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption("War in Cosmo")
myColor = pygame.Color(0, 0, 0)
fpsClock = pygame.time.Clock()
FPS = 15

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

v_pos = [0, 100]
v_direcao = [4, 0]
pygame.draw.circle(DISPLAYSURF, WHITE, v_pos, 10)




while True:
    DISPLAYSURF.fill(BLACK)
    v_pos = np.add(v_pos, v_direcao)
    pygame.draw.circle(DISPLAYSURF, WHITE, v_pos, 10)


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                v_direcao = np.add(v_direcao, [-1, 0])
            if event.key == pygame.K_RIGHT:
                v_direcao = np.add(v_direcao, [1, 0])
            if event.key == pygame.K_UP:
                v_direcao = np.add(v_direcao, [0, -1])
            if event.key == pygame.K_DOWN:
                v_direcao = np.add(v_direcao, [0, 1])
        else:
            v_direcao = [0, 0]









    pygame.display.update()