#snakepython
import pygame
from pygame.locals import *
BLACK = (0,0,0)
BACK_COLOR = (200,200,200)
LENGTH = 10

class Joint(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.rect.Rect(x_pos, y_pos, LENGTH, LENGTH)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def move_joint(self, dir):
            if dir == "w":
                self.rect = self.rect.move(0,-LENGTH)
            if dir == "s":
                self.rect = self.rect.move(0,LENGTH)
            if dir == "a":
                self.rect = self.rect.move(-LENGTH,0)
            if dir == "d":
                self.rect = self.rect.move(LENGTH,0)



    def get_joint():
        return(self.rect)

    def draw_joint(self, surface):
        pygame.draw.rect(surface, BLACK, self.rect)
