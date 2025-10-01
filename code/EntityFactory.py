#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import W_WIDTH, W_HEIGHT
from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position = (0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', position))
                    list_bg.append(Background(f'Level1Bg{i}', (W_WIDTH, 0) ))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, W_HEIGHT * 0.4 ))
            case 'Player2':
                return Player('Player2', (10, W_HEIGHT * 0.6 ))
            case 'Enemy1':
                return Enemy('Enemy1', (W_WIDTH + 10, random.randint(20, W_HEIGHT - 20)))
            case 'Enemy2':
                return Enemy('Enemy2', (W_WIDTH + 10, random.randint(20, W_HEIGHT - 20)))