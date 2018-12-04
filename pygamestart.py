import pygame
from pygame.locals import *
from sys import exit

background_image = './image/background.jpg'
sprite_image = './image/spit.png'

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image).convert()
sprite = pygame.image.load(sprite_image)

clock = pygame.time.Clock()
x, y = 100, 100
speed_x, speed_y = 150, 170

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed/1000
    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds

    # 到达边界后速度反向
    if x > 640 - sprite.get_width():
        speed_x = -speed_x
        x = 640 - sprite.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0

    if y > 480 - sprite.get_height():
        speed_y = -speed_y
        y = 480 - sprite.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0

    pygame.display.update()