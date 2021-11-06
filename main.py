# main.py

import pygame as pg
import sys
from GUI.Battle.screen import BattleBackground
from GUI.settings import *
from GUI.player_sprite import *
from GUI.teacher_sprite import *
from random import randint

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        pass

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.grass = pg.sprite.Group()
        self.tallgrass = pg.sprite.Group()
        self.teacher = pg.sprite.Group()
        for x in range(0, GRIDWIDTH):
            for j in range(0, GRIDHEIGHT):
                Grass(self, x, j)
        for x in range(5, 10):
            for j in range(5, 10):
                TallGrass(self, x, j)
        self.danger = [randint(0, GRIDWIDTH), randint(0, GRIDHEIGHT)]
        Teacher1(self, self.danger[0], self.danger[1])
        self.player = Player(self, 5, 5)

    def battle(self):
        self.all_sprites = pg.sprite.Group()
        self.background = pg.sprite.Group()
        BattleBackground(self, 0, 0)

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
        if(self.player.x == self.danger[0] and self.player.y == self.danger[1]):
            self.battle()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
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