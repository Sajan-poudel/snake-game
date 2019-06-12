import pygame
from snake import Snake
from food import  Food
from extra import Extra
# from level import Level

pygame.init()
surf_width = 800
surf_height = 600
clock = pygame.time.Clock()

dis_surf = pygame.display.set_mode((surf_width, surf_height))
pygame.display.set_caption("snake game")

medium_font = pygame.font.Font(None, 35)


run = True
def score(score):
    text = medium_font.render("SCORE: "+ str(score), True, (230,230,230))
    dis_surf.blit(text, (0,0))


def game_loop():
    game = Snake(dis_surf)
    food = Food(dis_surf, surf_width, surf_height)
    # level = Level(dis_surf, surf_width, surf_height)
    extra = Extra(dis_surf)
    while run:
        dis_surf.fill((255, 255, 255))
        # dis_surf.fill((0, 0, 0))
        food.draw(game.x, game.y)
        # print(food.snake_lenght)
        game.draw(food.snake_lenght)
        score(food.snake_lenght - 1)
        # level.level_1()
        # print(game.width)
        if game.again:
            game_loop()

        pygame.display.update()
        clock.tick(30)

game_loop()
pygame.quit()
quit()


