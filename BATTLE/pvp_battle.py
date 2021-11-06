# pvp_battle.py
# written by David McCabe

'''
This program holds the logic for the fighting backend between two Fighters
'''

from SCP.Fighter.Fighter import Fighter
from SCP.Move.MovesList import MoveList
from GUI.Battle.screen import Battle_Screen
import random

# Reads user fighter data in user_info.txt
def read_info():
    user_info = dict()
    with open("user_info.txt", "r") as g:
        for i in g.readlines():
            split = i.index(":")
            user_info[i[:split]] = i[split + 2:].strip()
        user_info["Moves"] = [x.strip() for x in user_info["Moves"].split(",")]
    return user_info

# Returns instance of Fighter
def make_fighter(name, level, attack, defense, health, moves):
    return Fighter(name, level, attack, defense, health, moves)

# Returns size 2 array: (successful attack), (target fainted)
def Attack(Attacker, Target, Move):
    target_damage = 0
    success_chance = 1
    if random.random() < success_chance:
        Target.Damage(target_damage)
        if Target.IsDead():
            return True, True
        else:
            return True, False
    else:
        return False, False

# Runs Battle functions
# Returns True if user wins, else False
def Battle(user, fighter2):
    move_list = MoveList()
    f2_poss_moves = fighter2.getMoves()
    f2_total_moves = len(f2_poss_moves)
    while(not user.IsDead() and not fighter2.IsDead()):
        sc = Battle_Screen()
        next_move = move_list(sc.move_select())
        # Chooses a random move from the possible moves of computer
        f2_move = move_list(f2_poss_moves[random.randint(0, f2_total_moves - 1)])
        if random.random() > .5:
            outcome = Attack(user, fighter2, next_move)
            if fighter2.IsDead(): break
            outcome  = Attack(fighter2, user, f2_move)
        else:
            outcome  = Attack(fighter2, user, f2_move)
            if user.IsDead(): break
            outcome = Attack(user, fighter2, next_move)
    if not user.IsDead(): return True
    return False


