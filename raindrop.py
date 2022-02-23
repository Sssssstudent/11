import sys
import pygame
from pygame.sprite import Sprite
from rain import Rain

class Raindrop():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.screen_color = (156, 137, 200)
        pygame.display.set_caption('Raindrop')

        self.drops = pygame.sprite.Group()

        self._create_drops()


    def run(self):
        while True:
            self._check_event()
            self._update_drop()
            self._update_screen()


    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()


    def _update_screen(self):
        self.screen.fill(self.screen_color)
        self.drops.draw(self.screen)
        pygame.display.flip()


    def _create_drops(self):
        drop = Rain(self)
        drop_width, drop_height = drop.rect.size
        number_drops = self.screen_width // (2 * drop_width)
        number_rows = self.screen_height // (2 * drop_height)

        for row_number in range(number_rows):
            for drop_number in range(number_drops):
                self._create_drop(drop_number, row_number)


    def _create_drop(self, drop_number, row_number):
        drop = Rain(self)
        drop_width, drop_height = drop.rect.size
        drop.x = (drop_width + 2 * drop_width * drop_number)
        drop.rect.x = drop.x
        drop.rect.y = (drop_height + 2 * drop_height * row_number)
        self.drops.add(drop)

    def _update_drop(self):
        self.drops.update()



if __name__ == '__main__':
    rn = Raindrop()
    rn.run()



