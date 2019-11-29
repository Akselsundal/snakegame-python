# -*- coding: utf-8 -*-
import pygame
import math
from Joint import *
#from Snake import *
from pygame.locals import *
import random


pygame.font.init() #Initiating possibility for text in pygame
font = "freesansbold.ttf"
font_size = 30
font_color = JOINT_COLOR

#Function for formatting text, returns a rendered font and an rect which belongs to the text surface
def text_format(message, textFont, textSize, textColor, centerx, centery):
    newFont=pygame.font.SysFont(textFont, textSize)
    new_text=newFont.render(message, 0, textColor)
    new_rect = new_text.get_rect()
    new_rect.center =  (centerx, centery)
    return (new_text, new_rect)


def start_menu(surf):
    running = True
    intro = True
    ts1, ts1_rect = text_format("Velkommen til slangespelet", "/Users/akselsundal/sync/prosjekt/snakespel_python/lemon_milk/LemonMilk.otf", 20, JOINT_COLOR, BOARD_LENGTH/2*JOINT_LENGTH, 2*JOINT_LENGTH)
    surf.blit(ts1, ts1_rect)

    ts2, ts2_rect = text_format("Vel kva nivå du ynskjer å spele på:", "/Users/akselsundal/sync/prosjekt/snakespel_python/lemon_milk/LemonMilk.otf", 18, JOINT_COLOR, BOARD_LENGTH/2*JOINT_LENGTH, 6*JOINT_LENGTH)
    surf.blit(ts2, ts2_rect)

    ts3, ts3_rect = text_format("1: lett, 2: medium, 3: vanskeleg", "/Users/akselsundal/sync/prosjekt/snakespel_python/lemon_milk/LemonMilk.otf", 18, JOINT_COLOR,  BOARD_LENGTH/2*JOINT_LENGTH, 10*JOINT_LENGTH)
    surf.blit(ts3, ts3_rect)

    pygame.display.update()

    #Waiting for keypress, and recognizing it
    while (intro):
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.type == pygame.QUIT:
                running = False
                return (running)

            if pygame.key.name(event.key) not in ["1","2","3"]:
                continue
            else:
                intro = False
            #Setting speed to the chosen difficulty
    return(running)

#The game over screen, when you lose
def game_over(surf, points):
    surf.fill(BACK_COLOR)
    running = True
    choose = True
    ts1, ts1_rect = text_format("Du tapte!", "/Users/akselsundal/sync/prosjekt/snakespel_python/lemon_milk/LemonMilk.otf", JOINT_LENGTH*5/2, (200,0,0), BOARD_LENGTH/2*JOINT_LENGTH, 4*JOINT_LENGTH)
    surf.blit(ts1, ts1_rect)

    ts2, ts2_rect = text_format("Du fekk " + str(points) + " poeng", "/Users/akselsundal/sync/prosjekt/snakespel_python/lemon_milk/LemonMilk.otf", JOINT_LENGTH*5/2, JOINT_COLOR, BOARD_LENGTH/2*JOINT_LENGTH, 10*JOINT_LENGTH)
    surf.blit(ts2, ts2_rect)
    pygame.display.update()

    while choose:
        if pygame.event.get(pygame.QUIT):
            choose = False
            running = False

        for e in pygame.event.get(pygame.KEYDOWN):
            if pygame.key.name(e.key) == "r":
                choose = False
            else:
                choose = False
                running = False #Quit on "any"-key
    return(running)


print(pygame.font.get_fonts())
