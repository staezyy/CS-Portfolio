import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False
 
clock = pygame.time.Clock()

rect_x = 50
rect_y = 50

rect_change_x = 3
rect_change_y = 3
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x <0:
        rect_change_x = rect_change_x * -1
        
    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, [rect_x, rect_y, 50, 50])
    rect_x += rect_change_x
    rect_y += rect_change_y
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
