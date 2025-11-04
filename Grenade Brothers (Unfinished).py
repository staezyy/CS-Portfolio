import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, walls):
        super().__init__()
        self.image = pygame.Surface([70, 90])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_x = 0
        self.change_y = 0
        self.walls = walls

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Grenade(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, players, walls):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_y = 5
        self.change_x = 5
        self.players = players
        self.walls = walls

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.left <= 15 or self.rect.right >= SCREEN_WIDTH - 15:
            self.change_x *= -1

        if self.rect.top <= 15 or self.rect.bottom >= SCREEN_HEIGHT - 15:
            self.change_y *= -1

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
                self.change_x *= -1
            else:
                self.rect.left = block.rect.right
                self.change_x *= -1

all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

# players
player = Player(150, 490, wall_list)
all_sprite_list.add(player)

player2 = Player(580, 490, wall_list)
all_sprite_list.add(player2)

players = [player, player2]

# barriers
wall = Wall(0, 0, 15, 600) #left wall barrier
all_sprite_list.add(wall)
wall_list.add(wall)

wall = Wall(785, 0, 15, 600) #right wall barrier
all_sprite_list.add(wall)
wall_list.add(wall)

wall = Wall(0, 0, 800, 15) #top barrier
all_sprite_list.add(wall)
wall_list.add(wall)

wall = Wall(0, 585, 800, 15) #bottom barrier
all_sprite_list.add(wall)
wall_list.add(wall)


# walls
wall = Wall(385, 300, 15, 290) #middle barrier
all_sprite_list.add(wall)
wall_list.add(wall)

# grenade
grenade = Grenade(380, 150, 25, 25, players, wall_list)
all_sprite_list.add(grenade)

pygame.init()

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Grenade Brothers")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player2.changespeed(-6, 0 )
            if event.key == pygame.K_RIGHT:
                player2.changespeed(6, 0)

            if event.key == pygame.K_a:
                player.changespeed(-6, 0)
            if event.key == pygame.K_d:
                player.changespeed(6, 0)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player2.changespeed(6, 0)
            if event.key == pygame.K_RIGHT:
                player2.changespeed(-6, 0)

            if event.key == pygame.K_a:
                player.changespeed(6, 0)
            if event.key == pygame.K_d:
                player.changespeed(-6, 0)
    
    all_sprite_list.update()
    
    screen.fill(BLACK)

    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
