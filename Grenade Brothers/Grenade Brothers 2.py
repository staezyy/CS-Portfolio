#Eric Blair
#5/23/24
#Computer Science I
#New Albany High School

import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, walls):
        super().__init__()
        self.image = pygame.Surface([70, 20])
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
        self.change_x = random.choice([5, -5])
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
            if block == wall2.rect.top:
                self.change_y *= -1

        block_hit_list = pygame.sprite.spritecollide(self, player_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.change_y *= -1

all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()

# players
player = Player(150, 540, wall_list)
all_sprite_list.add(player)
player_list.add(player)

player2 = Player(580, 540, wall_list)
all_sprite_list.add(player2)
player_list.add(player2)

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

wall3 = Wall(0, 585, 800, 15) #bottom barrier
all_sprite_list.add(wall3)
wall_list.add(wall3)


# walls
wall2 = Wall(385, 300, 15, 290) #middle barrier
all_sprite_list.add(wall2)
wall_list.add(wall2)

# grenade
grenade = Grenade(380, 150, 25, 25, players, wall_list)
all_sprite_list.add(grenade)

pygame.init()

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
screen2 = pygame.display.set_mode(size)

pygame.display.set_caption("Grenade Brothers")

done = False

Score1 = 0
Score2 = 0

clock = pygame.time.Clock()

font = pygame.font.SysFont('minionproregularopentype', 25, False, False)
instructions = font.render("Player 1 must use the A and D keys to move left and right.", True, WHITE)
instructions2 = font.render("Player 2 must use the left and right arrow keys to move left and right.", True, WHITE)
instructions3 = font.render("Do NOT let the grenade touch the ground on your side", True, WHITE)

play = pygame.image.load("G:\My Drive\Grenade Brothers\PlayButton.jpg").convert()
play= pygame.transform.scale(play, [200, 200])
play.set_colorkey(BLACK)

vincent = pygame.image.load("G:\My Drive\Grenade Brothers\Vincent.png").convert()
vincent.set_colorkey(WHITE)
vincent = pygame.transform.scale(vincent, [269, 322])

leo = pygame.image.load("G:\My Drive\Grenade Brothers\Leo.png").convert()
leo.set_colorkey(WHITE)
leo = pygame.transform.scale(leo, [300, 300])

awo = pygame.image.load("aWayOut.png").convert()
awo.set_colorkey(BLACK)
awo = pygame.transform.scale(awo, [480, 270])

circle = pygame.image.load("G:\My Drive\Grenade Brothers\circle.png").convert()
circle.set_colorkey(BLACK)
circle = pygame.transform.scale(circle, [200, 200])

sound = pygame.mixer.Sound("G:\My Drive\Grenade Brothers\Doom.mp3")

done1 = False
soundplay = False

game_over = False
restart_prompt = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player2.changespeed(-6, 0)
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
            if event.key == pygame.K_e:
                if not soundplay:
                    sound.play()
                    soundplay = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            done1 = True
   
    if done1:
        all_sprite_list.update()
       
        # Grenade hits bottom barrier
        if grenade.rect.bottom >= SCREEN_HEIGHT - 15:
            if grenade.rect.centerx <= SCREEN_WIDTH - 415:
                Score1 += 1
            elif grenade.rect.centerx >= SCREEN_WIDTH - 400:
                Score2 += 1
            game_over = True
            # Reset grenade position
            grenade.rect.x = 380
            grenade.rect.y = 150
            grenade.change_x = random.choice([5, -5])
            grenade.change_y = 5
            done1 = False

    screen.fill(BLACK)

    if not done1:
        screen.blit(awo, [150, -50])
        screen.blit(instructions, [50, 150])
        screen.blit(instructions2, [50, 200])
        screen.blit(instructions3, [50, 250])
        screen.blit(circle, [285, 325])
        screen.blit(play, [285, 325])
        screen.blit(vincent, [5, 300])
        screen.blit(leo, [499, 300])
    else:
        all_sprite_list.draw(screen)

    # Scores
    score_text = font.render(f"Player 1 Score: {Score1} | Player 2 Score: {Score2}", True, WHITE)
    screen.blit(score_text, [15, 15])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# Other programs used: Maze Game, Homescreen, Graphics and Sound Intro
