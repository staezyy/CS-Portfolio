import pygame
import random
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
COQUELICOT = (255, 56, 0)
AMARANTH = (159, 43, 104)

class Player(pygame.sprite.Sprite):
    def __init__(self,color, w, h):
        super().__init__()
        self.image = pygame.Surface([w, h ])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
pygame.init()

bad_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(10):
    bad = Player(AMARANTH, 30, 30)
    bad.rect.x = random.randrange(700)
    bad.rect.y = random.randrange(500)
    bad_list.add(bad)
    all_sprites_list.add(bad)

good = Player(COQUELICOT, 20, 20)
all_sprites_list.add(good)
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False
 
clock = pygame.time.Clock()

score = 0
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pos = pygame.mouse.get_pos()
    good.rect.x = pos[0]-10
    good.rect.y = pos[1]-10
    caught_list = pygame.sprite.spritecollide(good, bad_list, True)
    for a in caught_list:
        score += 1
    print_score = str(score)
    font = pygame.font.SysFont("Arial", 30, True, False)
    rendered_font = font.render("Score: " + print_score, True, BLACK)
 
    screen.fill(WHITE)

    screen.blit(rendered_font, [400, 20])

    all_sprites_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
