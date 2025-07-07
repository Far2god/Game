import pygame
import json
from constants import *
from lava import *

class World:
    def __init__ (self, lvl_name, lava_group):
        with open (f"levels/{lvl_name}", "r") as file:
            data = json.load(file)
        dirt_img = pygame.image.load("images/world/tile4.png")
        grass_img = pygame.image.load("images/world/tile1.png")
        self.tile_list = []
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1 or tile == 2:
                    images = {1: dirt_img, 2: grass_img}
                    img = pygame.transform.scale(images[tile], (TILE_SIZE, TILE_SIZE))

                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                elif tile == 3:
                    lava = Lava(col_count * TILE_SIZE,
                                row_count * TILE_SIZE + (TILE_SIZE // 2 ))
                    lava_group.add(lava)
                    #self.tile_list.append(lava)
                col_count += 1
            row_count += 1
