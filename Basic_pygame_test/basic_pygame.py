import pygame
from Sprite_Services.Basic_player import Player
from Sprite_Services.Market_Stall import MarketStall
from Sprite_Services.Buttons import Button


from Basic_player import Player
from Market_Stall import MarketStall
import constants

# Game initialization
pygame.init()
screen = pygame.display.set_mode(constants.size)
pygame.display.set_caption("2D Top-Down Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # None uses the default font, size 36

# Game objects
player = Player()
market_stall = MarketStall()
temp_button = Button("Test button",100,100,50,50)

all_sprites = pygame.sprite.Group()
market_stalls = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(market_stall)
all_sprites.add(temp_button)

# Main game loop
running = True
show_portfolio = False  # Flag to toggle portfolio visibility
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Handles game closing
            running = False
        elif event.type == MARKET_COLLISION_EVENT:
            print("Custom Event: Collision detected with Market Stall!")
            # Handle market stall collisions here <---
        elif event.type == pygame.KEYDOWN:
            # Toggle portfolio visibility when SPACE is pressed
            if event.key == pygame.K_SPACE:
                show_portfolio = not show_portfolio

    # stores the (x,y) coordinates into
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()
    player.update(keys)

    collisions = pygame.sprite.spritecollide(player, market_stalls, False)
    if collisions:
        if not collision_occurred:
            collision_occurred = True
            pygame.event.post(pygame.event.Event(MARKET_COLLISION_EVENT))
    else:
        collision_occurred = False

    screen.fill((255, 255, 255))  # Clear screen
    all_sprites.draw(screen)  # Draw sprites
    # Show the player's portfolio if the flag is true
    if show_portfolio:
        display_portfolio(player.portfolio, screen, font)

    pygame.display.flip()  # Refresh display
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()



