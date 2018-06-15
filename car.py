import pygame
import random
import math
from brain import Brain

class Car(Brain):

    def __init__(self, weights):
        self.rect = pygame.Rect(315.0, 240.0, 10.0, 10.0)
        self.color = (255, 255, 255)
        super(Car, self).__init__(weights)

    def move(self, dx):
        self.rect.x += dx

    def check_colision(self, borders):
        if borders is None:
            return True
        for obj in borders:
            if self.rect.colliderect(obj):
                return True
        return False

    def parse_borders(self, borders):
        left_dist = self.rect.x - (borders[0].x + borders[0].width)
        right_dist = borders[1].x - (self.rect.x + self.rect.width)
        return [left_dist/150, right_dist/150]

    def border_score(self, borders_dist):
        score = 0
        for border in borders_dist:
            score += (1 - abs(abs(border) - 0.5))/2
        return score

    def drive(self, borders):
        borders_dist = self.parse_borders(borders)
        score = self.border_score(borders_dist)
        delta = self.think(borders_dist)
        delta = 200 * (delta - 0.5)
        self.move(round(delta))
        return delta, score
