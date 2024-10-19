import pygame

from Buttons import Button, Sell_button, Buy_button

from Minable_model import Minable
from Basic_player import Player
from Market_Stall import MarketStall
import constants
import pygraph
import csv_reader

# Game initialization
pygame.init()
screen = pygame.display.set_mode(constants.size)
pygame.display.set_caption("Stock Starter")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # None uses the default font, size 36
collection_cooldown = 60
market_cooldown = 60

# Game objects
Gold_pile = Minable(constants.Gold_path, constants.Gold_pos)
Iron_pile = Minable(constants.Iron_path, constants.Iron_pos)
Coal_pile = Minable(constants.Coal_path, constants.Coal_pos)
player = Player()
market_stall = MarketStall()
background = pygame.image.load(constants.Background_path).convert()

"""BUTTONS"""
gold_buy = Buy_button("0", 100, 100, 600, 50, player.portfolio)
iron_buy = Buy_button("1", 100, 100, 600, 150, player.portfolio)
coal_buy = Buy_button("2", 100, 100, 600, 250, player.portfolio)
gold_sell = Sell_button("0", 100, 100, 500, 50, player.portfolio)
iron_sell = Sell_button("1", 100, 100, 500, 150, player.portfolio)
coal_sell = Sell_button("2", 100, 100, 500, 250, player.portfolio)

# temp_button = Sell_button("Test button",100,100,50,50,player.portfolio)


all_sprites = pygame.sprite.Group()
market_stalls = pygame.sprite.Group()
piles = pygame.sprite.Group()

# Button sprites
buttons = [gold_buy, iron_buy, coal_buy, gold_sell, iron_sell, coal_sell]
for b in buttons:
    all_sprites.add(b)

all_sprites.add(player)
all_sprites.add(market_stall)
all_sprites.add(Gold_pile)
all_sprites.add(Coal_pile)
all_sprites.add(Iron_pile)
piles.add(Gold_pile, Iron_pile, Coal_pile)
market_stalls.add(market_stall)


# Graphing & data initialization
reader = csv_reader.CSVReader()
data = reader.get_stock("IBM")
grapher = pygraph.Grapher(screen, data)

# custom collision event
MARKET_COLLISION_EVENT = pygame.USEREVENT + 1
PILE_COLLISION_EVENT = pygame.USEREVENT + 2

# initializing collision flag
market_collision_occurred = False


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
draw_graph = False  # Flag to draw the graph
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Handles game closing
            running = False
        elif event.type == MARKET_COLLISION_EVENT:
            # print("Custom Event: Collision detected with Market Stall!")
            draw_graph = True

        elif event.type == pygame.KEYDOWN:
            # Toggle portfolio visibility when SPACE is pressed
            if event.key == pygame.K_SPACE:
                show_portfolio = not show_portfolio
        elif event.type == PILE_COLLISION_EVENT:
            print("Collision with pile detected")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()  # Get click position
            for b in buttons:

                if b.on_button(x,y):
                    print("Button clicked.")
                    b.click(grapher)



    if collection_cooldown > 0:
        collection_cooldown -= 1
    if market_cooldown > 0:
        market_cooldown -= 1
    if market_cooldown == 0:
        grapher.update()
        market_cooldown = 60

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()
    player.update(keys)

    market_collisions = pygame.sprite.spritecollide(player, market_stalls, False)
    if market_collisions:
        if not market_collision_occurred:
            market_collision_occurred = True
            pygame.event.post(pygame.event.Event(MARKET_COLLISION_EVENT))
    else:
        draw_graph = False
        market_collision_occurred = False

    if collection_cooldown == 0:
        piles_collision = pygame.sprite.spritecollideany(player, piles)
        if piles_collision:
            if piles_collision == Gold_pile:
                player.portfolio.add_gold(constants.Gold_add)
            elif piles_collision == Iron_pile:
                player.portfolio.add_iron(constants.Iron_add)
            elif piles_collision == Coal_pile:
                player.portfolio.add_coal(constants.Coal_add)
        collection_cooldown = 60
        collision_occurred = False

    screen.fill((255, 255, 255))  # Clear screen
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)  # Draw sprites
    # Show the player's portfolio if the flag is true
    if show_portfolio:
        display_portfolio(player.portfolio, screen, font)

    if draw_graph:
        grapher.draw()

    pygame.display.flip()  # Refresh display
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()
