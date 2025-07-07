import pygame
from player import Player
from world import World
from  constants import *
from buttons import Button

# Инициализируем экран
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

lava_group = pygame.sprite.Group()
world = World("lvl_1.json", lava_group)
# Инициализируем игрока
player = Player(lava_group)
player.rect.left = TILE_SIZE
player.rect.bottom = HEIGHT - TILE_SIZE

bg_image = pygame.image.load("images/world/bg12.png")
bg_rect = bg_image.get_rect()

restart_button = Button(WIDTH // 2, HEIGHT // 2, "images/buttons/restart_btn.png")

run = True
while run:
    display.blit(bg_image, bg_rect)

    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Update player
    player.update(world.tile_list)
    #костыль
    for tile in world.tile_list:
        display.blit(tile[0], tile[1])
    lava_group.draw(display)
    lava_group.update()
    #Отрисовка игрока
    display.blit(player.image, player.rect)

    if player.game_state == -1:
        display.blit(restart_button.image, restart_button.rect)
        if restart_button.draw():
            for l in lava_group:
                l.kill()
            lava_group.empty()
            player = Player(lava_group)
            world = World("lvl_1.json", lava_group)
            player.game_state = 0
            player.rect.left = TILE_SIZE
            player.rect.bottom = HEIGHT - TILE_SIZE

    pygame.display.flip()
    clock.tick(40)