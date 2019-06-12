import pygame
from snake import Snake
import random

apple = pygame.image.load('apple.png')

class Food():

    def __init__(self, dis_surf, surf_width, surf_height):
        self.snake = Snake(dis_surf)
        self.dis_surf = dis_surf
        self.surf_width = surf_width
        self.surf_height = surf_height
        self.foodx = random.randrange(0 , self.surf_width - self.snake.height)
        self.foody = random.randrange(0, self.surf_height - self.snake.height)
        self.snake_lenght = 1

    def draw(self, snake_x, snake_y):
        self.dis_surf.blit(apple, (self.foodx, self.foody))
        # pygame.draw.rect(self.dis_surf, (255, 0, 0), (self.foodx, self.foody, self.snake.height, self.snake.height))
        self.con(snake_x, snake_y)

    def con(self, snake_x, snake_y):
        if snake_x >= self.foodx and snake_x <= self.foodx + self.snake.height:
            if snake_y >= self.foody and snake_y <= self.foody + self.snake.height:
                self.foodx = random.randrange(0, self.surf_width - self.snake.height)
                self.foody = random.randrange(0, self.surf_height - self.snake.height)
                self.snake_lenght+=1

            elif snake_y + self.snake.height >= self.foody and snake_y + self.snake.height <= self.foody + self.snake.height:
                self.foodx = random.randrange(0, self.surf_width - self.snake.height)
                self.foody = random.randrange(0, self.surf_height - self.snake.height)
                self.snake_lenght += 1

        elif snake_x + self.snake.height >= self.foodx and snake_x +self.snake.height <= self.foodx + self.snake.height:
            if snake_y >= self.foody and snake_y <= self.foody + self.snake.height:
                self.foodx = random.randrange(0, self.surf_width - self.snake.height)
                self.foody = random.randrange(0, self.surf_height - self.snake.height)
                self.snake_lenght += 1

            elif snake_y + self.snake.height > self.foody and snake_y + self.snake.height < self.foody + self.snake.height:
                self.foodx = random.randrange(0, self.surf_width - self.snake.height)
                self.foody = random.randrange(0, self.surf_height - self.snake.height)
                self.snake_lenght += 1

        # print(snake_x, " ", self.foodx, "------", snake_y, " ", self.foody)



