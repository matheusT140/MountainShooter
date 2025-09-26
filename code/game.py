#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import W_WIDTH, W_HEIGHT, MENU_OPTION
from code.menu import Menu
from code.level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[3]:
                pass
            else:
                pygame.quit()
                quit()
            pass

