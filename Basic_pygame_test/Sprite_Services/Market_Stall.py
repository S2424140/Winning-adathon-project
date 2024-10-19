import pygame
from Basic_pygame_test import constants


class MarketStall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the market stall image
        self.stall_image = pygame.image.load(constants.Market_Stall_path).convert_alpha()

        # Load the shadow image
        self.shadow_image = pygame.image.load(constants.Market_Stall_Shadow_path).convert_alpha()

        stall_width, stall_height = self.stall_image.get_width(), self.stall_image.get_height()
        shadow_width, shadow_height = self.shadow_image.get_width(), self.shadow_image.get_height()

        # Create a surface big enough to fit both the stall and the shadow
        combined_width = max(stall_width, shadow_width)
        combined_height = shadow_height + stall_height  # Stack the images vertically with some offset

        self.combined_image = pygame.Surface((combined_width, combined_height), pygame.SRCALPHA)

        # Blit the shadow and then the stall onto the combined surface
        shadow_offset_y = 23
        shadow_offset_x = -12
        self.combined_image.blit(self.shadow_image, (shadow_offset_x, shadow_offset_y))  # Draw shadow first
        self.combined_image.blit(self.stall_image, (0, 0))  # Draw stall on top of the shadow

        # Use the combined surface as the sprite's image
        self.image = self.combined_image

        # Get the rect for the new combined image
        self.rect = self.image.get_rect()

        # Position the stall at the top-middle of the screen
        self.rect.midtop = (constants.width // 2, 0)
