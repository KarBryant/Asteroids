import pygame, constants

class ScoreDisplay:
    def __init__(self, font_size:int, position: tuple, color=(255,255,255)):
        self.color = color
        self.font_size = font_size
        self.position = position
        self.font = pygame.font.SysFont(None, font_size)

        
    def render(self, screen, score_variable):
        self.text = self.font.render(f"Score: {score_variable}",True, self.color)
        return screen.blit(self.text, (self.position[0],self.position[1]))
