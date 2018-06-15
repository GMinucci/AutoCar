import pygame
import json
from pygame.locals import *
from road import Road

pygame.init()
width, height = 640, 480
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

road = Road(with_mouse=True, drawing=True)
last_pos = 320

while 1:
    display.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(road.mouse_map)
            pygame.quit()
            exit(0)
        if pygame.mouse.get_pressed()[0]:
          last_pos, _ = pygame.mouse.get_pos()

    road.draw(display)
    road.move_map(last_pos)

    pygame.display.flip()
    clock.tick(60)
