import pygame
from pygame.sprite import Sprite



class Rain(Sprite):
    def __init__(self, rn_game):
        super().__init__()
        self.screen = rn_game.screen
        self.rect = self.screen.get_rect()

        self.image = pygame.image.load('/Users/alexv/raindrop/drop.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

        self.drop_speed = 1.0

    def update(self):
        self.y += self.drop_speed
        self.rect.y = self.y





