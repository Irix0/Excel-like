import pygame
import pygame_textinput
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
            rect = pygame.Rect(x * (100 + 2) + 20, y * (60 + 2) + 60, 100, 60)
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
    print('Still looping')
    # If user close window :
    for event in pygame.event.get():
        # VIDEO RESIZE EVENT
        if event.type == pygame.VIDEORESIZE:
            old_surface_saved = window
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            # On the next line, if only part of the window
            # needs to be copied, there's some other options.
            window.blit(old_surface_saved, (0, 0))
            del old_surface_saved

        # MOUSE BUTTON DOWN EVENT
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                rectangle_position = Rectangle(event.pos)
                if plus_circle.collidepoint(event.pos):
                    columns += 1
                elif rectangle_position.is_ok(columns, rows):
                    w, h = window.get_size()
                    sub_surface = window.subsurface((0, 0, w, h)).copy()
                    text_input = pygame_textinput.TextInput(font_family='Roboto', text_color='WHITE', cursor_color='WHITE', font_size=30)
                    z = True
                    while z:
                        window.blit(sub_surface, (0, 0))
                        events = pygame.event.get()
                        text_input.update(events)
                        window.blit(text_input.get_surface(), (rectangle_position.get_rectangle_x(columns), rectangle_position.get_rectangle_y(rows)))
                        # print(rectangle_position.get_rectangle_x(columns))
                        pygame.display.flip()

                        if text_input.update(events):  # TextInput.update return True if K_RETURN pressed
                            window = sub_surface
                            window.blit(window, (0, 0))
                            del sub_surface
                            z = False

        # QUIT EVENT
        elif event.type == pygame.QUIT:
            pygame.quit()
            running = False
