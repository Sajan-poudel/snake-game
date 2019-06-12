import pygame
# medium_font = pygame.font.Font(None, 35)
# large_font = pygame.font.Font(None, 60)

class Extra():

    def __init__(self, dis_surf):
        self.dis_surf = dis_surf

    def pause(self):
        paused = True
        self.posi("PAUSED press c to continue")
        pygame.display.update()
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

    def text_draw(self, mesg):
        text = pygame.font.Font(None, 35).render(mesg, True, (0, 0, 0))
        return text, text.get_rect()

    def posi(self, mesg):
        text, text_rect = self.text_draw(mesg)
        text_rect.center = (400, 300)
        self.message(text, text_rect)

    def score(self):
        text = medium_font.render("SCORE: " + str(score), True, (216, 162, 62))
        self.message(text, (0,0))

    def message(self, mesg, pos):
        self.dis_surf.blit(mesg, pos)