# -*- coding: utf-8 -*-
import pygame
from Joint import *
from Snake import *
from pygame.locals import *


CLOCK = pygame.time.Clock()
pressed_key =   {"w": False,
                "s": False,
                "a": False,
                "d": False}



class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 600, 600
        self.n = 0

    def on_init(self):
        #------------------------------
        #Lager Surface
        #------------------------------
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Snake Spel, av Aksel")
        self._display_surf.fill(BACK_COLOR)

        #-----------------------------
        #Lager og teikner Slange
        #------------------------------

        self.snake = Snake()
        self.key = None
        pygame.display.flip()
        self._running = True


    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            else:
                if event.type == pygame.KEYDOWN:
                    for key in pressed_key:
                        if key == pygame.key.name(event.key):
                            self.key = key
                            pressed_key[key] = True
                            self.snake.move_snake(key)


    def on_loop(self):
        self.snake.move_snake(self.key)



    def on_render(self):
        self._display_surf.fill(BACK_COLOR)

        self.snake.draw_snake(self._display_surf)
        pygame.display.update()
        pygame.time.wait(100)

    def on_cleanup(self):
        pygame.quit()



#--------------------------------------------------
#                THE GAME LOOP
#--------------------------------------------------

    def game_loop(self):

        while(self._running):
            if pygame.event.peek(pygame.QUIT):
                self._running = False


            if pygame.event.peek(pygame.KEYDOWN):
                self.on_event()

            else:
                self.on_loop()


            self.on_render()



    def on_execute(self):

        if self.on_init() == False:
            self._running = False

        else:
            self.game_loop()

        self.on_cleanup()




if __name__ == "__main__":
    the_app = App()
    print("videre fra APP")
    the_app.on_execute()
