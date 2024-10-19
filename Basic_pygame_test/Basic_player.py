import pygame
import constants, Portfolio_model


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(constants.D_Idle_path).convert_alpha()  # determines Players sprite

        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Initial position
        self.portfolio = Portfolio_model.Portfolio(constants.Starter_Gold, constants.Starter_Iron,
                                                   constants.Starter_Coal,
                                                   constants.Starter_Money)

    def getPortfolio(self):
        return self.portfolio

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




