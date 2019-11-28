#snakepython
import pygame
from pygame.locals import *

JOINT_COLOR = (250,250,250)
BACK_COLOR = (100,100,100) #Defining color of background


JOINT_LENGTH = 16
SPACE = 2
BOARD_LENGTH = 20

FRUIT_LENGTH = JOINT_LENGTH
FRUIT_COLOR = (136, 204, 0)
class Joint(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos

    def find_dir(self, dir):
            if (dir == "up"):
                return([0,-1])
            if (dir == "down"):
                return([0,1])
            if  (dir == "left"):
                return([-1, 0])
            if  (dir == "right"):
                return([1, 0])

    def set_xy(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def draw_fruit(self, surface):
        self.rect = (self.x_pos*JOINT_LENGTH, self.y_pos*JOINT_LENGTH, JOINT_LENGTH-SPACE, JOINT_LENGTH-SPACE)

        pygame.draw.rect(surface, FRUIT_COLOR, self.rect)


    def draw_joint(self, surface):
        self.rect = (self.x_pos*JOINT_LENGTH, self.y_pos*JOINT_LENGTH, JOINT_LENGTH-SPACE, JOINT_LENGTH-SPACE)
        pygame.draw.rect(surface, JOINT_COLOR, self.rect)
