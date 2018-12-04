from pygame import *
import pygame
import sys

pygame.init()


screen = pygame.display.set_mode((640, 480), 0, 32)

img = r'./img/p1tankU.gif'

x = 320
play1 = pygame.image.load(img)
y = 480 - play1.get_width()
direction = 'U'


bollet = pygame.image.load(r'./img/enemymissile.gif')
b_x = 0
b_y = 0

while True:
    screen.fill((255, 255, 255))


    for e in event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                direction = 'L'
                x -= 10
                img = r'./img/p1tankL.gif'
            elif e.key == K_RIGHT:
                direction = 'R'
                x += 10
                img = r'./img/p1tankR.gif'
            elif e.key == K_UP:
                direction = 'U'
                y -= 10
                img = r'./img/p1tankU.gif'
            elif e.key == K_DOWN:
                direction = 'D'
                y += 10
                img = r'./img/p1tankD.gif'

            if e.key == K_SPACE:
                if direction == 'U':
                    b_x = x + play1.get_width()/2 - bollet.get_width()/2
                    b_y = y - bollet.get_width()
                elif direction == 'D':
                    b_x = x + play1.get_width()/2 - bollet.get_width()/2
                    b_y = y + play1.get_height() - bollet.get_width()/2
                elif direction == 'L':
                    b_x = x - bollet.get_width()/2
                    b_y = y + play1.get_height()/2 - bollet.get_width()/2
                elif direction == 'R':
                    b_x = x + play1.get_width() - bollet.get_width()/2
                    b_y = y + play1.get_height()/2 - bollet.get_width()/2

    play1 = pygame.image.load(img)
    screen.blit(play1, (x, y))
    screen.blit(bollet, (b_x, b_y))
    pygame.display.update()


