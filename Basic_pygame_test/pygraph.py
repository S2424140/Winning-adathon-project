import pygame
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from io import BytesIO

class Grapher:
    def __init__(self, screen, data, destination=(0,0)):
        self.dest = destination
        self.screen = screen

        self.data = iter(data[28:])
        self.x_data = np.arange(28)
        self.y_data = data[:28]

        self.fig, self.ax = plt.subplots()
        self.ln, = plt.plot([], [], 'b', animated=True)

        self.ax.set_xlim(1, 28)
        self.ax.set_ylim(0, max(data))

        self.update()


    def update(self):
        self.y_data = np.delete(self.y_data,0)
        self.y_data = np.append(self.y_data, next(self.data))
        self.ln.set_data(self.x_data, self.y_data)
        self.fig_to_surface()

    def fig_to_surface(self):
        buf = BytesIO()
        self.fig.savefig(buf, format="png")
        buf.seek(0)
        self.surface = pygame.image.load(buf)

    def set_destination(self, destination):
        self.dest = destination

    def draw(self):
        self.screen.blit(self.surface, self.dest)


# # example usage:
# pygame.init()
# clock = pygame.time.Clock()

# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))

# running = True
# grapher = Grapher(screen)
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     grapher.draw()

#     # Cap the frame rate
#     clock.tick(30)

