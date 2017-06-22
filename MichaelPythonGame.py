import pygame
import math
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
SKY = (135, 206, 250)
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("A Super Kewl Game")

PI = 3.141592653

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(SKY)            
 
    # --- Game logic should go here
    
    # --- Drawing code should go here
    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, GREEN, [[350,21], [300,400], [450,400]], 75)
    pygame.draw.rect(screen, BROWN, [325, 200, 80, 500])
    pygame.draw.rect(screen, GREEN, [0, 475, 700, 25])
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    # Draw on the screen several lines from (0, 10) to (100, 110)
    # 5 pixels wide using a while loop
    y_offset = 0
    
