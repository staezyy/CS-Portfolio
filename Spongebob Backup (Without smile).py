import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,243,96)
BROWN = (180,122,61)
BLUE = (126,181,232)
YELLOW2 = (191, 174, 21)
RED = (230,58,58)
 
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
 
    screen.fill(WHITE)
#Spongebob build
    pygame.draw.rect(screen, YELLOW, [250,108, 150, 240])
    pygame.draw.rect(screen, BROWN, [250, 300, 150, 50])
    pygame.draw.rect(screen, WHITE, [250, 270, 150, 30])
    pygame.draw.rect(screen, BLACK, [255, 317, 30, 12])
    pygame.draw.rect(screen, BLACK, [295, 317, 60, 12])
    pygame.draw.rect(screen, BLACK, [365, 317, 30, 12])

#Shoes
    pygame.draw.circle(screen, BLACK, [290, 420], 10)
    pygame.draw.ellipse(screen, BLACK, [260, 410, 35, 25])
    pygame.draw.circle(screen, BLACK, [365, 420], 10)
    pygame.draw.ellipse(screen, BLACK, [360, 410, 35, 25])

#Socks
    pygame.draw.rect(screen, BLACK, [285, 385, 10, 35], 2)
    pygame.draw.rect(screen, BLACK, [360, 385, 10, 35], 2)

#Legs
    pygame.draw.rect(screen, YELLOW, [285, 350, 10, 35])
    pygame.draw.rect(screen, YELLOW, [360, 350, 10, 35])

#Pants
    pygame.draw.rect(screen, BROWN, [275, 350, 35, 15])
    pygame.draw.rect(screen, BROWN, [345, 350, 35, 15])

#outline
    pygame.draw.line(screen, BLACK, [250, 108], [250, 350], 3)
    pygame.draw.line(screen, BLACK, [250, 108], [400, 108], 3)
    pygame.draw.line(screen, BLACK, [400, 108], [400, 350], 3)
    pygame.draw.line(screen, BLACK, [250, 350], [400, 350], 3)

#Tie
    pygame.draw.rect(screen, RED, [317, 270, 15, 15])
    pygame.draw.line(screen, RED, [320, 281], [310, 315], 10)
    pygame.draw.line(screen, RED, [327, 281], [337, 315], 10)
    pygame.draw.rect(screen, RED, [320, 285, 10, 20])
    pygame.draw.rect(screen, RED, [317, 298, 17, 20])
    pygame.draw.line(screen, RED, [342, 316], [325, 330], 23)
    pygame.draw.line(screen, RED, [306, 315], [325, 330], 23)
    

#Teeth
    pygame.draw.rect(screen, WHITE, [310, 231, 12, 15])
    pygame.draw.rect(screen, WHITE, [325, 231, 12, 15])

#Spongebob mouth
    pygame.draw.ellipse(screen, BLACK, [273, 155, 105, 78], 3)
    
#Spongebob Cut off half ellipse for smile
    pygame.draw.rect(screen, YELLOW, [272, 155, 112, 50])

#Spongebob Eyelashes
    pygame.draw.line(screen, BLACK, [353, 150], [353, 135], 5)
    pygame.draw.line(screen, BLACK, [297, 150], [297, 135], 5)
    pygame.draw.line(screen, BLACK, [285, 150], [280, 137], 5)
    pygame.draw.line(screen, BLACK, [341, 150], [336, 137], 5)
    pygame.draw.line(screen, BLACK, [365, 150], [370, 137], 5)
    pygame.draw.line(screen, BLACK, [309, 150], [315, 137], 5)
    
#Spongebob eyes
    pygame.draw.circle(screen, BLACK, [297, 175], 30, 3)
    pygame.draw.circle(screen, BLACK, [353, 175], 30, 3)
    pygame.draw.circle(screen, WHITE, [297, 175], 27)
    pygame.draw.circle(screen, WHITE, [353, 175], 27)
    pygame.draw.circle(screen, BLACK, [302, 177], 15, 3)
    pygame.draw.circle(screen, BLACK, [348, 177], 15, 3)
    pygame.draw.circle(screen, BLUE, [302, 177], 12)
    pygame.draw.circle(screen, BLUE, [348, 177], 12)
    pygame.draw.circle(screen, BLACK, [302, 177], 7)
    pygame.draw.circle(screen, BLACK, [348, 177], 7)
    pygame.draw.circle(screen, WHITE, [298, 172], 3)
    pygame.draw.circle(screen, WHITE, [344, 172], 3)
    pygame.draw.circle(screen, WHITE, [304, 182], 2)
    pygame.draw.circle(screen, WHITE, [351, 182], 2)
#outline of spongebob
    
#Spongebob nose
    pygame.draw.ellipse(screen, YELLOW, [315, 180, 22, 30])
    pygame.draw.ellipse(screen, BLACK, [315, 180, 22, 30], 3)
    pygame.draw.rect(screen, YELLOW, [318, 192, 10, 20])

#Sponge Circles
    pygame.draw.circle(screen, YELLOW2, [263, 130], 10)
    pygame.draw.circle(screen, YELLOW2, [260, 150], 5)
    pygame.draw.circle(screen, YELLOW2, [390, 130], 7)
    pygame.draw.circle(screen, YELLOW2, [380, 240], 12)
    pygame.draw.circle(screen, YELLOW2, [370, 260], 4)
    pygame.draw.circle(screen, YELLOW2, [265, 245], 6)
    pygame.draw.circle(screen, YELLOW2, [278, 258], 7)

 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
