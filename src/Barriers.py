import pygame
import random

class Barriers:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.margin = 75
        self.barrier_length = 150
        self.thickness = 12
        self.vert_lines = []
        self.horz_lines = []
        self.vertical_grid = []
        for k in range((self.screen.get_height() - (2 * self.margin)) // self.barrier_length):
            sub_grid = []
            for j in range(((self.screen.get_width() - (2 * self.margin)) // self.barrier_length) - 1):
                if random.randint(1, 100) <= 45:
                    sub_grid.append(True)
                else:
                    sub_grid.append(False)
            self.vertical_grid.append(sub_grid)
        self.horizontal_grid = []
        for i in range((self.screen.get_width() - (2 * self.margin)) // self.barrier_length):
            sub_grid = []
            for l in range(((self.screen.get_height() - (2 * self.margin)) // self.barrier_length) - 1):
                if random.randint(1, 100) <= 45:
                    sub_grid.append(True)
                else:
                    sub_grid.append(False)
            self.horizontal_grid.append(sub_grid)


        for k in range(len(self.vertical_grid)):
            for j in range(len(self.vertical_grid[k])):
                if self.vertical_grid[k][j]:
                    self.vert_lines.append(pygame.Rect((self.margin + (self.barrier_length * (j + 1))) - (self.thickness // 2),
                                                       self.margin + (self.barrier_length * k),
                                                       self.thickness,
                                                       self.barrier_length))

        for k in range(len(self.horizontal_grid)):
            for j in range(len(self.horizontal_grid[k])):
                if self.horizontal_grid[k][j]:
                    self.horz_lines.append(pygame.Rect(self.margin + (self.barrier_length * k),
                                                       (self.margin + (self.barrier_length * (j + 1))) - (self.thickness // 2),
                                                       self.barrier_length,
                                                       self.thickness))
        self.lines = self.vert_lines + self.horz_lines

    def draw(self):
        for line in self.lines:
            pygame.draw.rect(self.screen, (139, 121, 94), line)


