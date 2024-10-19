import pygame
import sys
from Basic_player import Player
import constants

# Game initialization
pygame.init()
screen = pygame.display.set_mode(constants.size)
pygame.display.set_caption("2D Top-Down Game")
clock = pygame.time.Clock()

# Game objects
player = Player()
all_sprites = pygame.sprite.Group(player)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Handles game closing
            running = False

    
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 

        
    keys = pygame.key.get_pressed()
    player.update(keys)

    screen.fill((255, 255, 255))  # Clear screen
    all_sprites.draw(screen)  # Draw sprites

    pygame.display.flip()  # Refresh display
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()
