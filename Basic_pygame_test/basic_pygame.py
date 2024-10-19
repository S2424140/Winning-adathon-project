import pygame
from Sprite_Services.Basic_player import Player
from Sprite_Services.Market_Stall import MarketStall
from Sprite_Services.Buttons import Button

import constants

# Game initialization
pygame.init()
screen = pygame.display.set_mode(constants.size)
pygame.display.set_caption("2D Top-Down Game")
clock = pygame.time.Clock()

# Game objects
player = Player()
market_stall = MarketStall()
temp_button = Button("Test button",100,100,50,50)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(market_stall)
all_sprites.add(temp_button)

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
