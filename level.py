import pygame
from snake import Snake


class Level:
    def __init__(self, dis_surf, surf_width, surf_height):
        self.snake = Snake(dis_surf)
        self.dis_surf = dis_surf
        self.surf_width = surf_width
        self.surf_height = surf_height

class Level_1:
    if self.x < 0:
        self.x = 800
    elif self.x > 800:
        self.x = 0
    elif self.y < 0:
        self.y = 600
    elif self.y > 600:
        self.y = 0
