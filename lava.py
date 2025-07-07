import pygame.sprite

from constants import *


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        lava_img = pygame.image.load("images/world/lava.png")
        self.image = pygame.transform.scale(lava_img,
                                            (TILE_SIZE, TILE_SIZE // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y