import pygame
import sys
from Basic_player import Player


# Game initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2D Top-Down Game")
clock = pygame.time.Clock()

# Game objects
player = Player()
all_sprites = pygame.sprite.Group(player)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    screen.fill((255, 255, 255))  # Clear screen
    all_sprites.draw(screen)  # Draw sprites

    pygame.display.flip()  # Refresh display
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()