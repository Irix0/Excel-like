import pygame
import numpy as np
from components import *

# Init and settings
pygame.init()

size = width, height = 1920, 1000
title = "Window"
background = "#252525"
window = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption(title)

running = True

# Creating table
rows = 10
columns = 10
table = table(rows, columns)

# Loop till false
while running:
    # Set background
    window.fill(background)
    # Create grid
    for y in range(0, rows):
        for x in range(0, columns):
            rect = pygame.Rect(x * (100 + 2) + 20, y * (65 + 1) + 50, 100, 60)
            pygame.draw.rect(window, "#414141", rect)

    # ADD COLUMNS BUTTON
    plus = pygame.image.load('code/plus.png')
    plus = pygame.transform.scale(plus, (100, 100))
    plus_circle = pygame.draw.circle(window, "#3e3636", (100 + (columns * 101), 500), 45)
    window.blit(plus, (50 + (columns * 101), 450))

    # INFOS
    columns_text = pygame.font.SysFont("Lucida Sans", 30)
    columns_text = columns_text.render("Columns : {}".format(columns), True, '#d72323', )
    window.blit(columns_text, (10, 10))
    rows_text = pygame.font.SysFont("Lucida Sans", 30)
    rows_text = rows_text.render("Columns : {}".format(rows), True, '#d72323', )
    window.blit(rows_text, (250, 10))
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if plus_circle.collidepoint(event.pos):
                    columns += 1
                if rect.collidepoint(event.pos):
                    print(rect.x)
                    print(rect.y)
        elif event.type == pygame.QUIT:
            pygame.quit()
            running = False
