import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (254,130, 140)
 
pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False
 
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        screen.fill(YELLOW)
        pygame.draw.ellipse(screen, WHITE, [250,150,50,100])
        pygame.draw.ellipse(screen, WHITE, [400,150,50,100])
        pygame.draw.circle(screen, BLACK, [350,350], 50)
        pygame.draw.circle(screen, BLACK, [275,200], 25)
        pygame.draw.circle(screen, BLACK, [425,200], 25)
        pygame.draw.rect(screen, BLACK, [250,100,50,25])
        pygame.draw.rect(screen, BLACK, [400,100,50,25])
        pygame.draw.circle(screen, YELLOW, [275,126], 25)
        pygame.draw.circle(screen, YELLOW, [425,126], 25)
        pygame.draw.circle(screen, PINK, [250,275], 35)
        pygame.draw.circle(screen, PINK, [450,275], 35)

        pygame.display.flip()
 
        clock.tick(60)
 
pygame.quit()
