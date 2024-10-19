import pygame
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from io import BytesIO
import sys

class Grapher:
    def __init__(self, destination=(0,0)):
        self.dest = destination

        self.x_data = np.arange(28)
        self.y_data = np.random.random(28)*100

        self.fig, self.ax = plt.subplots()
        self.ln, = plt.plot([], [], 'b', animated=True)

        self.ax.set_xlim(1, 28)
        self.ax.set_ylim(0, 100)

    def update(self):
        self.y_data = np.delete(self.y_data,0)
        self.y_data = np.append(self.y_data,np.random.random((1))*100)
        self.ln.set_data(self.x_data, self.y_data)
        self.fig_to_surface()

    def fig_to_surface(self):
        buf = BytesIO()
        self.fig.savefig(buf, format="png")
        buf.seek(0)
        self.surface = pygame.image.load(buf)

    def draw(self):
        self.update()
        screen.blit(self.surface, self.dest)
        pygame.display.flip()


pygame.init()
clock = pygame.time.Clock()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

running = True
grapher = Grapher()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grapher.draw()

    # Cap the frame rate
    clock.tick(30)

