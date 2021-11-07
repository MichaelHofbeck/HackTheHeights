from GUI.image_resizer import image_resizer
from SCP.Move.MovesList import moveType
from random import choice, randint
import pygame as pg

class Fighter:
    
    def __init__(self, name, level, attack, defense, health, moves, maxhealth, sprite, experience = 0):
        self.name = name
        self.level = level
        self.attack = attack
        self.defense = defense
        self.health = health
        self.moves = moves
        self.maxhealth = maxhealth
        self.experience = experience
        self.sprite = sprite
        self.all_sprites = pg.sprite.Group()

    def addExperience(self, number):
        self.experience -= number
        if self.experience <= 0:
            self.levelUp()
        oldexp = self.experience
        self.experience = self.level * 5 + 10 + oldexp

    def fullHeal(self):
        self.health = self.maxhealth

    def Damage(self, damage):
        self.health -= damage
        if self.health > self.maxhealth:
            self.health = self.maxhealth

    def IsDead(self):
        if self.health <= 0:
            return True
        return False
    

    def levelUp(self):
        self.level += 1
        addTrue = False
        #adds a random new move to the users new moves
        while addTrue == False:
            if choice([moveType("user")]) not in self.moves:
                choice([self.newMove(moveType("user"))])
                addTrue = True
        self.attack += randint(5, 15)
        self.defense += randint(5, 15)
        self.health += randint(5, 15)
    
    def newMove(self, move):
        self.moves.append(move)

    def getMoves(self):
        return self.moves

    def stats(self):
        return 'Name: {}\n Level: {}\n Attack: {}\n Defense: {}\n Health: {}\n Moves: {}\n Maxhealth: {}\n'.format(self.name, self.level, self.attack, self.defense, self.health, self.moves, self.maxhealth)

    def add_sprite(self, filename):
        self.all_sprites = pg.sprite.Group()
        self.filepath = filename
        self.sprite = image_resizer(filename)
        self.image = pg.image.load(self.filepath[0:-4] + "-resized-opp.png")
        self.rect = self.image.get_rect()
    

# player = Fighter("Minh", 1, 5, 5, 10, [])
