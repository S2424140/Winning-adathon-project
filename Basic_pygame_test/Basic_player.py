import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # determines Players sprite
        self.image.fill((0, 255, 0))  # Color the player green
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Start at the center of the screen

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


# Create the player
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
