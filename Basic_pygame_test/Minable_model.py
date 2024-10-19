import pygame


class Minable(pygame.sprite.Sprite):
    def __init__(self, image_path, position):
        super().__init__()

        # Load the image for the minable object (coal, gold, or iron)
        self.image = pygame.image.load(image_path).convert_alpha()

        # Create a rect based on the image's size for positioning
        self.rect = self.image.get_rect()

        # Set the position of the minable object
        self.rect.topleft = position  # Set position (x, y) passed as a parameter
