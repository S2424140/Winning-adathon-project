import pygame
import constants

# Base class for a static button for a UI
class Button(pygame.sprite.Sprite):
    def __init__(self,id:str,bwidth:int,bheight:int,x:int,y:int)->None:
        super().__init__()
        self.image = pygame.Surface((bwidth, bheight))  # determines Players sprite
        self.image.fill((20, 20, 20))  # Color the button black
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Initial position

    # Function to check if a given coordinate is on the button
    def on_button(self,x:int,y:int)->bool: # Returns true if a coordinate is on the button, checking if the coordinates are inside it
        x1,y1 = self.rect.bottomleft
        x2,y2 = self.rect.topright
        return bool((x>x1) and (y<y1) and (x<x2) and (y>y2))

    # Override for whatever function the button is used for
    def click():
        pass


class Sell_button(Button):
    def __init__(self,)->None:
        super().__init__()

    def click():
        pass