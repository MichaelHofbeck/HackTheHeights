# screen.py
# Written by David McCabe

import pygame as pg
from GUI.settings import *
from GUI.image_resizer import *
from SCP.Fighter.Fighter import *
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
        self.open = True
        self.background = pg.Rect(x, y, self.rect.x, self.rect.y)

class BattleForegroundUser(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.grass
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.filepath = 'GUI/pngs/test-back.png'
        image_resizer(self.filepath[0:-8] + 'back.png', WIDTH // 4, HEIGHT // 4)
        self.image = pg.image.load(self.filepath[0:-4] + "-resized.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE + 25
        self.rect.y = y * TILESIZE + 375

class BattleForegroundOpponent(pg.sprite.Sprite):
    def __init__(self, game, opponent, x, y):
        self.groups = game.all_sprites, game.grass
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.filepath = opponent
        image_resizer(self.filepath, WIDTH // 4, HEIGHT // 4)
        self.image = pg.image.load(self.filepath[0:-4] + "-resized.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE + 525
        self.rect.y = y * TILESIZE + 75

def draw_moves(move_list, screen):
    font = pg.font.SysFont(None, 24)
    moves = get_user_moves()
    assert len(moves) <= 4, ("Too many Moves!!")
    for i, move_str in enumerate(moves):
        img = font.render(move_str, True, BLACK)
        screen.blit(img, (1000, 10+(i*150)))