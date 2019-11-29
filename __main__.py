# -*- coding: utf-8 -*-
import pygame
import math
from Joint import *
from Snake import *
from TextScreen import *
from pygame.locals import *
import random

#CLOCK = pygame.time.Clock() #Possibility for adding counter of time

#Defining directions for use with arrows
DIRECTIONS = {  "up": (0,-1),
        "down": (0,1),
        "left": (-1,0),
        "right": (1,0)}


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None #initiating the display surface
        #Setting size of board
        self.size = self.width, self.height = BOARD_LENGTH*JOINT_LENGTH, BOARD_LENGTH*JOINT_LENGTH

#-------------------------------------------------------------------------------------------------------------
    def on_init(self):
        pygame.init() #Initiating pygame
        random.seed(a=None) #Possibility for random ints
        self._display_surf = pygame.display.set_mode(self.size) #Making screen surface
        pygame.display.set_caption("Snake Spel, av Aksel") #Window caption
        self._display_surf.fill(BACK_COLOR) # Filling the screen with color

        self.snake = Snake() # Making the snake
        self.speed = 150 # Speed of snake

        pygame.font.init() #Initiating possibility for text in pygame
        self.dir = "down" #This is the start position and is updated in game
        self.new_dir = None #A temporary direction used in on_event()
        self.difficulty = 2 #The difficulty sets startingspeed (and maybe snake size)
        self.points = len(self.snake.skeleton)-3 # The points are defined by size of snake

        #Making the points-text
        self.points_text,self.points_text_rect  = self.text_format("Poeng: " + str(self.points), "freesansbold.ttf", 30, JOINT_COLOR, BOARD_LENGTH/2*JOINT_LENGTH, JOINT_LENGTH)
        self._display_surf.blit(self.points_text, self.points_text_rect)
        pygame.display.update()


        # Making the first fruit on random position
        self.rand_x = random.randint(1,BOARD_LENGTH-1)
        self.rand_y = random.randint(1,BOARD_LENGTH-1)
        self.fruit = Joint(self.rand_x, self.rand_y)

#Function for formatting text, returns a rendered font and an rect which belongs to the text surface
    def text_format(self, message, textFont, textSize, textColor, centerx, centery):
        self.newFont=pygame.font.Font(textFont, textSize)
        self.new_text=self.newFont.render(message, 0, textColor)
        self.new_rect = self.new_text.get_rect()
        self.new_rect.center =  (centerx, centery)
        return (self.new_text, self.new_rect)




#-------------------------------------------------------------------------------------------------------------
                            # "ON FUNCTIONS" (Happens every loop)
#-------------------------------------------------------------------------------------------------------------

    def on_event(self, events):
        for e in events: #Iterationg through all events concerning keypress
            self.new_dir = pygame.key.name(e.key) #Setting the temporary direction to the key, before checking
            self.old = False #This is set to True when I can't use the new_dir(if it is in the oposite direction)

            if pygame.key.name(e.key) in DIRECTIONS:
                if DIRECTIONS[self.new_dir][0]*DIRECTIONS[self.dir][0] == -1 or DIRECTIONS[self.new_dir][1]*DIRECTIONS[self.dir][1] == -1:
                    self.old = True

            elif pygame.key.name(e.key) not in DIRECTIONS: #If you pressed something that is not in DIRECTIONS
                self.old = True


            if self.old  == True: # If old is true, scrap the new direction
                self.snake.move_snake(self.dir)

            else: # Else use the new direction
                self.snake.move_snake(self.new_dir)
                self.dir = self.new_dir


    def on_loop(self): #Move the snake
        self.snake.move_snake(self.dir)



    def on_render(self):
        self._display_surf.fill(BACK_COLOR) # Fill background
        self.snake.draw_snake(self._display_surf) # Draw the snake again
        self.fruit.draw_fruit(self._display_surf) # Draw fruit again
        #Draw points text again
        self.points_text, self.point_text_rect = self.text_format("Poeng: " + str(self.points), "freesansbold.ttf", 20, JOINT_COLOR, (BOARD_LENGTH/2*JOINT_LENGTH), (JOINT_LENGTH))
        self._display_surf.blit(self.points_text, self.points_text_rect)
        pygame.display.update() #aaaand update display

    #This is called after loop
    def on_cleanup(self):

        pygame.quit()

#-------------------------------------------------------------------------------------------------------------
    #GAME FUNCTIONS
#-------------------------------------------------------------------------------------------------------------


    def eat_fruit(self): #Is called when fruit is eaten
        self.points += 1 #You get a point
        fruit_in_snake = True # Bool variable to make sure fruit dont spawn in snake
        print(self.points)

        while fruit_in_snake: #Try to place new fruit
            self.rand_x = random.randint(1,BOARD_LENGTH-1)
            self.rand_y = random.randint(1, BOARD_LENGTH-1)
            self.fruit.set_xy(self.rand_x, self.rand_y) #Setting new x and y pos
            for i in range(len(self.snake.skeleton)):
                if (self.snake.skeleton[i].x_pos != self.fruit.x_pos) and (self.snake.skeleton[i].y_pos != self.fruit.y_pos):
                    fruit_in_snake = False

        self.speed = self.snake.set_speed(self.difficulty, self.speed, self.points) #Set speed whith the updated points
        self.snake.eat_fruit = True



    def check_move(self): #Checks if the move means death (if snake is outside screen or in itself)
        if self.snake.skeleton[0].x_pos < 0 or self.snake.skeleton[0].x_pos > (BOARD_LENGTH-1):
            self._running = False
        if self.snake.skeleton[0].y_pos < 0 or self.snake.skeleton[0].y_pos > (BOARD_LENGTH-1):
            self._running = False
        for i in range(1,len(self.snake.skeleton)):
            if (self.snake.skeleton[0].x_pos == self.snake.skeleton[i].x_pos) and (self.snake.skeleton[0].y_pos == self.snake.skeleton[i].y_pos):
                self._running = False

        if (self.snake.skeleton[0].x_pos == self.fruit.x_pos) and (self.snake.skeleton[0].y_pos == self.fruit.y_pos):
            self.eat_fruit()




#--------------------------------------------------
#                THE GAME LOOP
#--------------------------------------------------

    def game_loop(self):
        while(self._running):
            if pygame.event.get(pygame.QUIT):
                self.on_cleanup()
            self.event_queue = pygame.event.get(pygame.KEYDOWN)
            if len(self.event_queue) >= 1:
                self.on_event(self.event_queue)
                self.check_move()


            else:
                self.on_loop()
                self.check_move()


            self.on_render()

            pygame.time.wait(self.speed)



    def draw_board(self):
        for i in range(BOARD_LENGTH):
            pygame.draw.rect(self._surface, JOINT_COLOR, k*JOINT_LENGTH, 0, JOINT_LENGTH, JOINT_LENGTH)
        for k in range(1, BOARD_LENGTH):
            pygame.draw.rect(self._surface,JOINT_COLOR,  0, k*JOINT_LENGTH, JOINT_LENGTH, JOINT_LENGTH)

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        else:
            start_menu(self._display_surf)
            self.game_loop()
        self._running = game_over(self._display_surf, self.points)
        self.on_cleanup()



ssss
if __name__ == "__main__":
    the_app = App()
    print("videre fra APP")
    the_app.on_execute()
