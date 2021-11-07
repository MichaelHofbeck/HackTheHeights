# screen.py
# Written by David McCabe

import pygame as pg
from GUI.settings import *
from GUI.image_resizer import *
from pvp_battle import get_user_moves

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

def Draw_moves(move_list, screen):
    font = pg.font.SysFont(None, 24)
    moves = get_user_moves()
    assert len(moves) <= 4, ("Too many Moves!!")
    for i, move_str in enumerate(moves):
        img = font.render(move_str, True, BLACK)
        screen.blit(img, (WIDTH*(980/1240), 10+(i*150)))
