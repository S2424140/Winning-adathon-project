import pygame
from Basic_pygame_test import constants


class MarketStall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the market stall image
        self.image = pygame.image.load(constants.Market_Stall_path).convert_alpha()
        self.rect = self.image.get_rect()
        # Position it at the top-middle of the screen
        self.rect.midtop = (constants.width // 2, 0)  # Centered horizontally at the top
