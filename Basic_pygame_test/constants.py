import os
import pygame

size = width, height = 800, 400
Starter_Money = 100
Starter_Gold = 0
Starter_Iron = 10
Starter_Coal = 20

Gold_add = 1
Coal_add = 10
Iron_add = 5

pile_size = pwidth, pheight = 100, 100

Background_path = "Assets/Background.png"
D_Idle_path = "Assets/Player-Animations/D_Idle.png"
Market_Stall_path = "Assets/Buildings/Objects/6 Tent/1.png"
Market_Stall_Shadow_path = "Assets/Buildings/Objects/1 Shadow/6.png"
Gold_path = "Assets/PileAssets/GoldPile.png"
Gold_pos = (width - pwidth - 10, height // 2 - pheight // 2)
Iron_path = "Assets/PileAssets/IronPile.png"
Iron_pos = (width - pwidth - 10, Gold_pos[1] + pheight + 10)
Coal_path = "Assets/PileAssets/CoalPile.png"
Coal_pos = (width - pwidth - 10, Gold_pos[1] - pheight - 10)
Sell_path = "Assets/Buttons/sell.png"
Buy_path = "Assets/Buttons/buy.png"
