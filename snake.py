import pygame
# from level import Level
from extra import Extra

img1 = pygame.image.load('snakehead.png')
img2 = pygame.image.load('snaketail.png')
class Snake():

    def __init__(self, dis_surf):
        self.dis_surf = dis_surf
        self.extra = Extra(self.dis_surf)
        self.x = 255
        self.y = 255
        self.width = 20
        self.height = 20
        self.x_change = 0
        self.y_change = 0
        self.vel = 10
        self.snake_list = []
        self.snake_head = []
        self.snake_lenght = 1
        self.go = 'right'
        self.direction = {'right':270, 'up':0, 'left':90, 'down':180}
        self.again = False
        self.gonna = False

    def run(self):
        head = pygame.transform.rotate(img1, self.direction[self.go])
        self.dis_surf.blit(head, (self.snake_list[-1][0], self.snake_list[-1][1]))
        for snake in self.snake_list[1:-1]:
            pygame.draw.rect(self.dis_surf, (0, 255, 0), (snake[0], snake[1], self.width, self.height))
        if not len(self.snake_list) == 1:
            tail = pygame.transform.rotate(img2, self.direction[self.go])
            self.dis_surf.blit(tail, (self.snake_list[0][0], self.snake_list[0][1]))

    def draw(self, snake_length):
        self.snake_lenght =snake_length
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and not self.go == 'left':
                    self.x_change = self.vel
                    self.y_change = 0
                    self.go = 'right'
                elif event.key == pygame.K_LEFT and not self.go == 'right':
                    self.x_change = -self.vel
                    self.y_change = 0
                    self.go = 'left'
                elif event.key == pygame.K_UP and not  self.go == 'down':
                    self.y_change = -self.vel
                    self.x_change = 0
                    self.go = 'up'
                elif event.key == pygame.K_DOWN and not self.go == 'up':
                    self.y_change = self.vel
                    self.x_change = 0
                    self.go = 'down'
                elif event.key == pygame.K_p:
                    self.extra.pause()

        self.x += self.x_change
        self.y += self.y_change

        if self.x < 0:
            self.x = 800 - self.width
        elif self.x > 800-self.width:
            self.x = 0
        elif self.y < 0:
            self.y = 600 - self.width
        elif self.y > 600 - self.width:
            self.y = 0

        self.snake_head = []
        self.snake_head.append(self.x)
        self.snake_head.append(self.y)
        self.snake_list.append(self.snake_head)

        if len(self.snake_list) > self.snake_lenght:
            del self.snake_list[0]

        if self.snake_head in self.snake_list[:-1]:
            self.extra.posi("GAME OVER!! PRESS C TO PLAY AGAIN!! ELSE Q TO QUIT")
            pygame.display.update()
            self.gonna = True
            while self.gonna:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.QUIT
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            self.again = True
                            self.gonna =False
                        if event.key == pygame.K_q:
                            pygame.quit()
                            quit()
        self.run()


