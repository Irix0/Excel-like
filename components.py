import pygame
import numpy as np

class table:
    def __init__(self, rows =20, columns=20):
        table_size = rows, columns
        self.rows = rows
        self.columns = columns
        self.table = np.eye(rows, columns)

    def get_rows(self):
        return self.rows
    def get_columns(self):
        return self.columns


