# main.py

import pygame as pg
import sys
from GUI.Battle.screen import BattleBackground
from GUI.settings import *
from GUI.player_sprite import *
from GUI.teacher_sprite import *
from GUI.tilemap import *
from random import randint
from pvp_battle import *
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        self.map = Map('Maps\map1.txt')

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.grass = pg.sprite.Group()
        self.tallgrass = pg.sprite.Group()
        self.teacher = pg.sprite.Group()
        self.battling = False
        for x in range(0, self.map.tilewidth):
            for j in range(0, self.map.tileheight):
                Grass(self, x, j)
        self.danger = [(randint(3, self.map.tilewidth - 3), randint(3, self.map.tileheight - 3))]
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    TallGrass(self, col, row)
                    self.danger += [(col, row)]

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'P':
                   self.player = Player(self, col, row, self.map.tilewidth, self.map.tileheight)
        Teacher1(self, self.danger[0][0], self.danger[0][1])
        self.dangersquares = len(self.danger)
        self.camera = Camera(self.map.width, self.map.height)

    def battle(self):
        self.battling = True
        self.all_sprites = pg.sprite.Group()
        self.background = pg.sprite.Group()
        BattleBackground(self, 0, 0)
        Battle(self.player, )

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        if(self.player.position == self.danger[0]):
            self.camera.reset()
            self.battle()
        for x in range(self.dangersquares):
            if self.player.position == self.danger[x]:
                if self.random_key == 5:
                    self.camera.reset()
                    self.battle()


    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if self.battling == False:
                    self.random_key = randint(0, 14)
                    if event.key == pg.K_ESCAPE:
                        self.quit()
                    if event.key == pg.K_LEFT:
                        self.player.move(dx=-1)
                    if event.key == pg.K_RIGHT:
                        self.player.move(dx=1)
                    if event.key == pg.K_UP:
                        self.player.move(dy=-1)
                    if event.key == pg.K_DOWN:
                        self.player.move(dy=1)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()