import pygame as pg
from PIL import Image
from GUI.settings import *
from GUI.image_resizer import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, boundary_x, boundary_y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.filepath = 'GUI/pngs/test-front.png'
        image_resizer(self.filepath)
        image_resizer(self.filepath[0:-9] + 'back.png')
        image_resizer(self.filepath[0:-9] + 'right.png')
        image_resizer(self.filepath[0:-9] + 'left.png')
        self.image = pg.image.load(self.filepath[0:-4] + "-resized.png")
        self.rect = self.image.get_rect()
        self.boundary_x = boundary_x
        self.boundary_y = boundary_y
        self.x = x
        self.y = y
        self.position = (self.x, self.y)

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy
            self.position = (self.x, self.y)
            if dy == -1:
                self.image = pg.image.load(self.filepath[0:-9] + "back-resized.png")
            elif dy == 1:
                self.image = pg.image.load(self.filepath[0:-4] + "-resized.png")
            elif dx == 1:
                self.image = pg.image.load(self.filepath[0:-9] + "right-resized.png")
            else:
                self.image = pg.image.load(self.filepath[0:-9] + "left-resized.png")

    def collide_with_walls(self, dx=0, dy=0):
        if (self.x + dx == self.boundary_x or self.x + dx == -1) or (self.y + dy == self.boundary_y or self.y + dy == -1):
            return True
        return False 

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
        self.filepath = 'GUI/pngs/grass.png'
        image_resizer(self.filepath)
        self.image = pg.image.load(self.filepath[0:-4] + "-resized.png")
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
        image_resizer(self.filepath)
        self.image = pg.image.load(self.filepath[0:-4] + "-resized.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE