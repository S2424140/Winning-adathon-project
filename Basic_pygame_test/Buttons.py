import pygame
import constants
import Portfolio_model
from pygraph import Grapher

# Base class for a static button for a UI
class Button(pygame.sprite.Sprite):
    def __init__(self,id:str,bwidth:int,bheight:int,x:int,y:int,img_path:str)->None: 
        super().__init__()
        self.img = pygame.transform.scale(pygame.image.load(img_path).convert_alpha(), (bwidth,bheight))
        self.image = pygame.Surface((bwidth, bheight), pygame.SRCALPHA)  # determines Players sprite
        # self.image = pygame.image.load(constants.Sell_path).convert_alpha()
        # self.image.fill((255, 20, 20))  # Color the button black
        self.image.blit(self.img, (0, 0))  
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
    def __init__(self,id:str,bwidth:int,bheight:int,x:int,y:int,port:Portfolio_model)->None:
        super().__init__(id,bwidth,bheight,x,y,constants.Sell_path)
        self.portfolio = port
        self.id = id

    def click(self,grapher:Grapher):
        p = self.portfolio
        price = grapher.get_price()
        try:
            match self.id:
                case "0":
                    p.remove_gold(1/price)
                    p.add_money(1)
                    print("Sold gold.")
                case "1":
                    p.remove_iron(1/price)
                    p.add_money(1)
                    print("Sold iron.")
                case "2":
                    p.remove_coal(1/price)
                    p.add_money(1)
                    print("Sold coal.")
        except:
            print("Invalid sell.")

class Buy_button(Button):
    def __init__(self,id:str,bwidth:int,bheight:int,x:int,y:int,port:Portfolio_model)->None:
        super().__init__(id,bwidth,bheight,x,y,constants.Buy_path)
        self.portfolio = port
        self.id = id

    def click(self,grapher:Grapher):
        p = self.portfolio
        price = grapher.get_price()
        try:
            match self.id:
                case "0":
                    p.add_gold(1*price)
                    p.remove_money(1)
                    print("Bought gold.")
                case "1":
                    p.add_iron(1*price)
                    p.remove_money(1)
                    print("Sold iron.")
                case "2":
                    print("")
                    p.add_coal(1*price)
                    p.remove_money(1)
                    print("Sold coal.")
        except:
            print("Invalid buy.")
