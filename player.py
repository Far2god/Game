import pygame.transform

# y = self.gravity

class Player:
    def __init__(self, lava_group):
        self.image = pygame.image.load("images/player/player1.png")
        self.image = pygame.transform.scale(self.image,(35, 70))
        self.rect = self.image.get_rect()
        self.speed_y = 0
        self.jumped = False
        self.game_state = 0
        #0 = игра продолжается. 1 = выиграли. -1 = проиграли
        self.lava_group = lava_group

    def update (self, tile_list):
        if self.game_state == 0:
            speed_x = 0
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                speed_x -= 4
            if key[pygame.K_RIGHT]:
                speed_x += 4
            if key[pygame.K_SPACE] and not self.jumped:
                self.speed_y = -15
                self.jumped = True

            for tile in tile_list:
                if tile[1].colliderect(self.rect.x + speed_x, self.rect.y, self.image.get_width(), self.image.get_height() ):
                    speed_x = 0
                if tile[1].colliderect(self.rect.x, self.rect.y + self.speed_y, self.image.get_width(), self.image.get_height() ):
                    if self.speed_y >= 0:
                        self.jumped = False
                    self.speed_y = 0


            self.rect.x += speed_x
            self.rect.y += self.speed_y

            if self.speed_y < 10:
                self.speed_y += 1

            if pygame.sprite.spritecollide(self, self.lava_group, False):
                self.game_state = -1

        elif self.game_state == -1:
           # print ("Game over")
            if self.rect.y > 0:
                self.rect.y -= 5
