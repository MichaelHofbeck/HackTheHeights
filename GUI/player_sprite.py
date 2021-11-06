import pygame as pg
from PIL import Image
from GUI.settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load('GUI/pngs/player_front.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Grass(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.grass
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.filepath = "GUI/pngs/grass.png"
        img = Image.open(self.filepath)
        resized_img = img.resize((GRIDHEIGHT * 2, GRIDHEIGHT * 2))
        resized_img.save(self.filepath)
        self.image = pg.image.load(self.filepath)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class TallGrass(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.grass
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.filepath = 'GUI/pngs/tallgrass.png'
        img = Image.open(self.filepath)
        resized_img = img.resize((GRIDHEIGHT * 2, GRIDHEIGHT * 2))
        resized_img.save(self.filepath)
        self.image = pg.image.load(self.filepath)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE