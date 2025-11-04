"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
From:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example
 
Explanation video: http://youtu.be/8IRyt7ft7zg
 
Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""
 
import pygame
 
# -- Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (219, 187, 42)
 
# Screen dimensions
SCREEN_WIDTH = 525
SCREEN_HEIGHT = 260
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Test')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

win_list = pygame.sprite.Group()

coin_list = pygame.sprite.Group()

#Coins

coin = Coin(75, 75, 15, 15)
all_sprite_list.add(coin)
coin_list.add(coin)

coin = Coin(175, 125, 15, 15)
all_sprite_list.add(coin)
coin_list.add(coin)

coin = Coin(330, 173, 15, 15)
all_sprite_list.add(coin)
coin_list.add(coin)

coin = Coin(383, 75, 15, 15)
all_sprite_list.add(coin)
coin_list.add(coin)

coin = Coin(485, 125, 15, 15)
all_sprite_list.add(coin)
coin_list.add(coin)

#Borders
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 250, 460, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(516, 0, 10, 590)
wall_list.add(wall)
all_sprite_list.add(wall)

#Walls

wall = Wall(50, 50, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 50, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 100, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(150, 10, 10, 100)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(100, 100, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(160, 100, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(210, 100, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(160, 150, 60, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 150, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 50, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(150, 150, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(60, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(210, 210, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(210, 50, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(260, 50, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(260, 100, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(310, 100, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(310, 150, 110, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(360, 150, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(270, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(260, 160, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(310, 210, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(410, 50, 10, 110)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(360, 50, 110, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(360, 50, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(460, 100, 60, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(460, 100, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(410, 200, 110, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(310, 0, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

win_block = Wall(460, 250, 57, 10)
win_list.add(win_block)
all_sprite_list.add(win_block)
win_block.image.fill(YELLOW)

win_list.add(win_block)
 
# Create the player paddle object
player = Player(25, 25)
player.walls = wall_list

end_num = 0

score = 0
 
all_sprite_list.add(player)
 
clock = pygame.time.Clock()

font = pygame.font.SysFont('minionproregularopentype', 25, False, False)
text = font.render("you Won!", True, WHITE)
 
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    end_list = pygame.sprite.spritecollide(player, win_list, False)
    for i in end_list:
        end_num += 1

    coins_collected = pygame.sprite.spritecollide(player, coin_list, True)

    for i in coins_collected:
        score += 1

    text2 = font.render("Score: " + str(score), True, WHITE)

    
 
    all_sprite_list.update()
 
    screen.fill(BLACK)

    all_sprite_list.draw(screen)

    if end_num > 0:
        screen.blit(text, [0, 0])
        player.change_x = 0
        player.change_y = 0

    screen.blit(text2, [0, 235])
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
