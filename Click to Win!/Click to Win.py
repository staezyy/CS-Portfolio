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
soundPlay = False
 
clock = pygame.time.Clock()

count = 0

bg = pygame.image.load("mustafar.jpg").convert() #background
bg = pygame.transform.scale(bg, [700,500]) #background

font = pygame.font.SysFont('minionproregularopentype', 50, False, False)
text = font.render("CLICK TO DIE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", True, WHITE)

text3 = font.render("YOU DIED!!!!!!!!", False, WHITE)

font2 = pygame.font.SysFont('minionproregularopentype', 20, False, False)

sound = pygame.mixer.Sound("explosion.ogg")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if not soundPlay:
                    sound.play()
                    soundPlay = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if count < 10:
                    count += 1
                
        
    text2 = font2.render("Counter: " + str(count), True, WHITE)

    screen.fill(WHITE)

    screen.blit(bg, [0,0]) #background
    screen.blit(text2, [0, 475])
    if count < 10:
        screen.blit(text, [15, 25])
    else:
        screen.blit(text3, [165, 25])
        
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
