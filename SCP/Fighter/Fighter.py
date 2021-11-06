from Move.MovesList import MoveList
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
        if self.level == 5:
            self.newMove(MoveList()["eyeroll"])
        if self.level == 10:
            self.newMove(MoveList()["homework finesse"])
        if self.level == 15:
            self.newMove(MoveList()["knowledge cram"])
        if self.level == 20:
            self.newMove(MoveList()["bitch slap"])
        self.attack += 14
        self.defense += 12
        self.health += 10
    
    def newMove(self, move):
        self.moves.append(move)

    def getMoves(self):
        return self.moves


    def stats(self):
        return 'Name: {}\n Level: {}\n Attack: {}\n Defense: {}\n Health: {}\n Moves: {}\n Maxhealth: {}\n'.format(self.name, self.level, self.attack, self.defense, self.health, self.moves, self.maxhealth)


