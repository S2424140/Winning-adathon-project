import pygame
import constants

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # determines Players sprite
        self.image.fill((0, 255, 0))  # Color the player green
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Initial position

    def update(self, keys):
        speed = 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed
        if keys[pygame.K_UP]:
            self.rect.y -= speed
        if keys[pygame.K_DOWN]:
            self.rect.y += speed
        # Keep the player within the screen bounds
        if self.rect.left < 0:
            self.rect.left = 0  # Prevent moving out from the left
        if self.rect.right > constants.width:
            self.rect.right = constants.width  # Prevent moving out from the right
        if self.rect.top < 0:
            self.rect.top = 0  # Prevent moving out from the top
        if self.rect.bottom > constants.height:
            self.rect.bottom = constants.height  # Prevent moving out from the bottom

# Create the player
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
