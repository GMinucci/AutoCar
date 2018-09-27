import pygame
import json
from pygame.locals import *
from road import Road
from car import Car

pygame.init()
width, height = 640, 480
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

weights_data = json.load(open('weights.txt'))
weights = weights_data["weights"]
best_bot_weight = [-0.9649205275728165, 0.13581275475099452, -1.5822522167855742, 1.9877229672881493, -1.1663725759796186, -2.9936308429223284, 0.19894375082619742, -0.6473870618447436, -1.2214740535884077, 0.3336941806985566]

font = pygame.font.SysFont("monospace", 20)
road = Road(with_mouse=False)
player = Car(weights)
# player = Car(best_bot_weight)

last_pos = 320
total_score = 0

while 1:
    display.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if pygame.mouse.get_pressed()[0]:
          last_pos, _ = pygame.mouse.get_pos()

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2)
    if key[pygame.K_RIGHT]:
        player.move(2)

    collided = player.check_colision(road.snap_map(player.rect.y))

    if collided:
        with open('score.txt', 'w') as outfile:
            json.dump({"value":total_score}, outfile)
            outfile.close()
        pygame.quit()
        exit(0)

    road.draw(display)
    dx, score = player.drive(road.snap_map(player.rect.y))
    total_score += score
    pygame.draw.rect(display, player.color, player.rect)

    if dx > 0:
        color = (122, 231, 199)
    else:
        color = (219, 84, 97)
    pygame.draw.rect(display, color, (5, 5, 55, 20))
    pygame.draw.rect(display, (134, 187, 216), (5, 30, 55, 20))
    label = font.render("%.4f" % dx, 1, (0, 0, 0))
    score_label = font.render("%.2f" % total_score, 1, (0, 0, 0))
    display.blit(label, (10, 10))
    display.blit(score_label, (10, 35))

    road.move_map(last_pos)

    pygame.display.flip()
    clock.tick(60)
