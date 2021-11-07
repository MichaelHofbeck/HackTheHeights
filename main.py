# main.py

from os import curdir
import pygame as pg
import sys
from time import sleep
from SCP.Fighter.Fighter import Fighter
from GUI.Battle.screen import *
from GUI.settings import *
from GUI.player_sprite import *
from GUI.teacher_sprite import *
from GUI.tilemap import *
from random import randint
from SCP.BushFIghters.BushFighters import *
from pvp_battle import *
from pvp_battle import get_user_moves_and_name, get_user_moves

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.battle_pos = None
        self.move_index = -1

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

    def reactivate(self):
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
        self.player = Player(self, self.curr_position[0], self.curr_position[1], self.map.tilewidth, self.map.tileheight)
        Teacher1(self, self.danger[0][0], self.danger[0][1])
        self.dangersquares = len(self.danger)
        self.camera = Camera(self.map.width, self.map.height)

    def battle_screen(self):
        if self.battle_pos != self.player.position:
            self.battling = True
            self.all_sprites = pg.sprite.Group()
            self.background = pg.sprite.Group()
            number_of_bushfighters = len(bush_fighters) - 1
            random_fighter = randint(0, number_of_bushfighters)
            opponent = bush_fighters[random_fighter]
            self.opponent_name = opponent.name
            opponent_sprite = bush_fighters[random_fighter].sprite
            BattleBackground(self, 0, 0)
            BattleForegroundUser(self, 0, 0)
            BattleForegroundOpponent(self, opponent_sprite, 0, 0)
            if self.move_index != -1:
                self.battle_mechanics(opponent)

    def battle_mechanics(self, opponent):
            # battlgebg.background()
            #Draw_moves(get_user_moves, self.screen)
            user = make_fighter()
            Battle(user, opponent, self.move_index)
            #Battle(make_fighter(), Fighter(name="Naomi", level=1, attack=5, defense=15, health=20, moves=["ramble and shamble"], experience=1, maxhealth=20))
            self.battle_pos = self.player.position
            if (user.IsDead() or opponent.IsDead()):
                self.battling = False
                self.move_index = -1
                self.reactivate()
                self.run()
        #sleep(5)

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
            self.curr_position = self.player.position
            self.battle_screen()
        for x in range(self.dangersquares):
            if self.player.position == self.danger[x]:
                if self.random_key == 5:
                    self.camera.reset()
                    self.curr_position = self.player.position
                    self.battle_screen()

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
        # moves drawing goes here
        if self.battling:
            draw_moves_and_names(self.screen, self.opponent_name)
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
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.battling == True:
                    pos = pg.mouse.get_pos()
                    if pos[0] > WIDTH*(980/1240):
                        if pos[1] < HEIGHT/4:
                            self.move_index = 0
                        elif pos[1] < HEIGHT/2:
                            self.move_index = 1
                        elif pos[1] < 3*HEIGHT/4:
                            self.move_index = 2
                        else:
                            self.move_index = 3
                        print(self.move_index)



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