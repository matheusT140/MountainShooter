#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(800, 600))

    def run(self, ):
        menu = Menu(self.window)
        menu.run()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close screen
                    quit()  # end pygame
