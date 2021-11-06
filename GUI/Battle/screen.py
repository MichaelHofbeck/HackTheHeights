# screen.py
# Written by David McCabe

import pygame as pg
from GUI.settings import *
from GUI.image_resizer import *

class BattleBackground(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.grass
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.filepath = 'GUI/pngs/battlebg.png'
        image_resizer(self.filepath, WIDTH, HEIGHT)
        self.image = pg.image.load(self.filepath[0:-4] + "-resized.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE