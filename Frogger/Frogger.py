import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Frog(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("G:/My Drive/Frogger/froggerdude.png")
        self.rect = self.image.get_rect()

pygame.init()

all_sprite_list = pygame.sprite.Group()

player = Frog(310, 460)
all_sprite_list.add(player)

player.rect.x = 310
player.rect.y = 460
player.image = pygame.transform.scale_by(player.image, (.1, .1))
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False
 
clock = pygame.time.Clock()

bg = pygame.image.load("G:/My Drive/Frogger/froggerbg.png")
bg= pygame.transform.scale(bg, [700, 500])

car = pygame.image.load("G:/My Drive/Frogger/froggercar.png")
car = pygame.transform.scale_by(car, (.3, .3))

move = 38.8

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= move
            elif event.key == pygame.K_RIGHT:
                player.rect.x += move
            elif event.key == pygame.K_UP:
                player.rect.y -= move
            elif event.key == pygame.K_DOWN:
                player.rect.y += move

    screen.fill(WHITE)

    screen.blit(bg, [0,0])
    screen.blit(car, [250, 290])

    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
