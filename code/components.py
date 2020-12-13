import pygame
import numpy as np


class Rectangle:
    def __init__(self, pos):
        self.x, self.y = pos

    def is_ok(self, columns, rows):
        if 20 < self.x < columns * (100 + 2) + 20 and 60 < self.y < rows * (60 + 2) + 60:
            return True
        else:
            return False

    def get_rectangle_x(self, columns):
        # Creating all list with all rect position (full left)
        a_list = []
        for x in range(0, columns):
            x = x * (100 + 2) + 20
            a_list.append(x)
        absolute_difference_function = lambda list_value: abs(list_value - self.x)
        closest_value = min(a_list, key=absolute_difference_function)
        # Comparison to always start input at full left
        if closest_value < self.x:
            return closest_value
        elif closest_value > self.x:
            return closest_value - 101

    def get_rectangle_y(self, rows):
        b_list = []
        for x in range(0, rows):
            x = x * (60 + 2) + 60
            b_list.append(x)
        absolute_difference_function = lambda list_value: abs(list_value - self.y)
        closest_value = min(b_list, key=absolute_difference_function)
        if closest_value < self.y:
            return closest_value
        elif closest_value > self.y:
            return closest_value - 61


class table:
    def __init__(self, rows=20, columns=20):
        table_size = rows, columns
        self.rows = rows
        self.columns = columns
        self.table = np.eye(rows, columns)

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns


rect = Rectangle((500, 20))

rect.get_rectangle_x(20)
