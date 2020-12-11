import pygame
import numpy as np
from components import *

# Init and settings
pygame.init()

size = width, height = 1920, 1000
title = "Window"
window = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption(title)

running = True

# Creating table
rows = 20
columns = 10
table = table(rows, columns)

# Loop till true

while running:
    # Set background
    window.fill("#252525")
    # Create grid
    for y in range(0, rows):
        for x in range(0, columns):
            rect = pygame.Rect(x * (50 + 1) + 20, y * (45 + 1) + 50, 50, 40)
            pygame.draw.rect(window, "#414141", rect)

    # ADD COLUMNS BUTTON
    plus_cirlce = pygame.draw.circle(window, "#525252", (100+(columns * 50), 500), 20)
    plus_vertical_line = pygame.draw.line(window, "#ca3e47", (85+(columns * 50), 500), (115+(columns * 50), 500))
    plus_horizontal_line = pygame.draw.line(window, "#ca3e47", (100+(columns * 50), 500+15), (100+(columns * 50), 500-15))



    pygame.display.flip()

    # If user close window :
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            old_surface_saved = window
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            # On the next line, if only part of the window
            # needs to be copied, there's some other options.
            window.blit(old_surface_saved, (0, 0))
            del old_surface_saved
        elif event.type == pygame.QUIT:
            pygame.quit()
            running = False
