import pygame
from pygame.locals import *
from Joint import *

FRUIT_COLOR = (46,139,87)
FRUIT_LENGTH = JOINT_LENGTH/2


class Fruit(Joint):

    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
