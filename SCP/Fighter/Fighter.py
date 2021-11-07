from SCP.Move.MovesList import moveType
from random import random

class Fighter:
    
    def __init__(self, name, level, attack, defense, health, moves, maxhealth, experience = 0):
        self.name = name
        self.level = level
        self.attack = attack
        self.defense = defense
        self.health = health
        self.moves = moves
        self.maxhealth = maxhealth
        self.experience = experience
        

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

    def IsDead(self):
        if self.health <= 0:
            return True
        return False
    

    def levelUp(self):
        self.level += 1
        addTrue = False
        #adds a random new move to the users new moves
        while addTrue == False:
            if moveType("user")[random.choice()] not in self.moves:
                self.newMove(moveType("user")[random.choice()])
                addTrue = True
        self.attack += random.randint(5, 15)
        self.defense += random.randint(5, 15)
        self.health += random.randint(5, 15)
    
    def newMove(self, move):
        self.moves.append(move)

    def getMoves(self):
        return self.moves


    def stats(self):
        return 'Name: {}\n Level: {}\n Attack: {}\n Defense: {}\n Health: {}\n Moves: {}\n Maxhealth: {}\n'.format(self.name, self.level, self.attack, self.defense, self.health, self.moves, self.maxhealth)

# player = Fighter("Minh", 1, 5, 5, 10, [])
