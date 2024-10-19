import pygame
from Basic_player import Player
from Market_Stall import MarketStall
from Buttons import Button, Sell_button


from Minable_model import Minable
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
Gold_pile = Minable(constants.Gold_path, constants.Gold_pos)
Iron_pile = Minable(constants.Iron_path, constants.Iron_pos)
Coal_pile = Minable(constants.Coal_path, constants.Coal_pos)
player = Player()
market_stall = MarketStall()
temp_button = Sell_button("Test button",100,100,50,50)

all_sprites = pygame.sprite.Group()
market_stalls = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(market_stall)
all_sprites.add(Gold_pile)
all_sprites.add(Coal_pile)
all_sprites.add(Iron_pile)
all_sprites.add(temp_button)
market_stalls.add(market_stall)

# custom collision event
MARKET_COLLISION_EVENT = pygame.USEREVENT + 1

# initializing collision flag
collision_occurred = False


# Function to display the portfolio interface
def display_portfolio(portfolio, screen, font):
    # Render the portfolio values
    gold_text = font.render(f"Gold: {portfolio.get_gold()}", True, (255, 215, 0))
    iron_text = font.render(f"Iron: {portfolio.get_iron()}", True, (192, 192, 192))
    coal_text = font.render(f"Coal: {portfolio.get_coal()}", True, (105, 105, 105))
    money_text = font.render(f"Money: ${portfolio.get_money()}", True, (0, 255, 0))

    # Blit (draw) the text onto the screen
    screen.blit(gold_text, (50, 50))
    screen.blit(iron_text, (50, 100))
    screen.blit(coal_text, (50, 150))
    screen.blit(money_text, (50, 200))


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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos() # Get click position
            print(temp_button.on_button(x,y))

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



